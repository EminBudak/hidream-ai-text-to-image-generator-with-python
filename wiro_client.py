import requests
import hmac
import hashlib
import time

class WiroClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.wiro.ai/v1"
        self.tool_slug = "wiro/text-to-image-hidreamai-i1"
    
    def generate_auth_headers(self):
        """Generate authentication headers for Wiro API"""
        nonce = str(int(time.time() * 1000))
        timestamp = str(int(time.time()))
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            (self.api_key + nonce + timestamp).encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
        return {
            'x-api-key': self.api_key,
            'x-nonce': nonce,
            'x-signature': signature
        }
    
    def submit_task(self, params):
        """Submit task to Wiro API"""
        try:
            headers = self.generate_auth_headers()
            headers['Content-Type'] = 'application/json'
            
            response = requests.post(
                f"{self.base_url}/Run/{self.tool_slug}",
                json=params,
                headers=headers
            )
            
            response.raise_for_status()
            data = response.json()
            
            if not data.get('result'):
                errors = data.get('errors', ['Unknown error'])
                raise Exception(f"Task submission failed: {', '.join(errors)}")
            
            return {
                'taskid': data.get('taskid'),
                'socketaccesstoken': data.get('socketaccesstoken')
            }
        except requests.exceptions.RequestException as e:
            raise Exception(f"Task submission failed: {str(e)}")
    
    def get_task_detail(self, task_id=None, socket_token=None):
        """Get task details using Task/Detail endpoint"""
        try:
            if not task_id and not socket_token:
                raise Exception('Either task_id or socket_token must be provided')
            
            headers = self.generate_auth_headers()
            headers['Content-Type'] = 'application/json'
            
            payload = {'socketaccesstoken': socket_token} if socket_token else {'taskid': task_id}
            
            response = requests.post(
                f"{self.base_url}/Task/Detail",
                json=payload,
                headers=headers
            )
            
            response.raise_for_status()
            data = response.json()
            
            if not data.get('result') or not data.get('tasklist') or len(data.get('tasklist', [])) == 0:
                raise Exception('Task not found or invalid response')
            
            return data['tasklist'][0]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get task detail: {str(e)}")
    
    def poll_task_result(self, socket_token, max_attempts=60, interval=2):
        """Poll task result until completion"""
        completed_statuses = ['task_postprocess_end', 'task_cancel']
        running_statuses = [
            'task_queue', 'task_accept', 'task_assign',
            'task_preprocess_start', 'task_preprocess_end',
            'task_start', 'task_output', 'task_postprocess_start', 'task_end'
        ]
        
        import time
        
        for attempt in range(max_attempts):
            try:
                task_detail = self.get_task_detail(socket_token=socket_token)
                status = task_detail.get('status')
                
                if status in completed_statuses:
                    if status == 'task_cancel':
                        raise Exception('Task was cancelled')
                    
                    # Extract result from outputs array
                    outputs = task_detail.get('outputs', [])
                    result = None
                    
                    for output in outputs:
                        if output.get('contenttype') == 'raw' and output.get('content', {}).get('answer'):
                            # LLM response with answer array
                            answer = output['content']['answer']
                            result = '\n\n'.join(answer) if isinstance(answer, list) else answer
                            break
                        elif output.get('url'):
                            # File output with URL
                            result = output['url']
                            break
                    
                    # Fallback to debugoutput
                    if not result and task_detail.get('debugoutput'):
                        result = task_detail['debugoutput']
                    
                    if not result:
                        raise Exception('No output found in task result')
                    
                    return result
                elif status not in running_statuses:
                    print(f"Warning: Unknown status: {status}")
                
                # Wait before next poll
                time.sleep(interval)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                time.sleep(interval)
        
        raise Exception('Polling timeout')
    
    def execute(self, params):
        """Execute tool with automatic polling"""
        try:
            print("🚀 Submitting task to Wiro API...")
            print(f"   Tool: {self.tool_slug}")
            print(f"   Parameters: {params}")
            
            # 1. Submit task
            task_info = self.submit_task(params)
            print(f"   ✅ Task submitted - ID: {task_info['taskid']}")
            
            # 2. Poll for result
            print("🔄 Polling for result...")
            result = self.poll_task_result(task_info['socketaccesstoken'])
            
            print("✅ Task completed!")
            return result
        except Exception as e:
            raise Exception(f"API execution failed: {str(e)}")
