import os
from wiro_client import WiroClient
from dotenv import load_dotenv

load_dotenv()

def main():
    client = WiroClient(os.getenv("WIRO_KEY"), os.getenv("WIRO_SECRET"))
    
    print("🚀 AI Untitled Tool - python")
    print(f"Running Untitled Tool...")
    print()
    
    # Parameters based on Untitled Tool API documentation
    params = {
    "prompt": "Example prompt"
}
    
    print("Parameters:", params)
    print()
    
    try:
        result = client.execute(params)
        print("✅ Result:", result)
    except Exception as error:
        print(f"❌ Error: {str(error)}")

if __name__ == "__main__":
    main()
