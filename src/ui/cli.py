import sys
from src.mcp.protocol import run_pipeline

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <target_name>")
        sys.exit(1)
    target_name = sys.argv[1]
    result = run_pipeline(target_name)
    print("Profile:", result['profile'])
    print("Context:", result['context'])
    print("Phishing Message:", result['message'])
    print("Risk Analysis:", result['risk'])
