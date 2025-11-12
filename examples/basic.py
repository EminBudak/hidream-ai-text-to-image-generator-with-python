import os
import json
from wiro_client import WiroClient
from dotenv import load_dotenv

load_dotenv()

def example():
    client = WiroClient(os.getenv("WIRO_KEY"), os.getenv("WIRO_SECRET"))
    
    print("📘 Example: AI Untitled Tool - python")
    print("Tool: Untitled Tool")
    print()
    
    # Example parameters from API documentation
    params = {
    "prompt": "Example prompt"
}
    
    print("Parameters:", json.dumps(params, indent=2))
    print()
    
    try:
        result = client.execute(params)
        print("✅ Success!")
        print("Result:", json.dumps(result, indent=2))
    except Exception as error:
        print(f"❌ Error: {str(error)}")

if __name__ == "__main__":
    example()
