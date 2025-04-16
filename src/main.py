from src.mcp.protocol import run_pipeline

if __name__ == "__main__":
           result = run_pipeline("Ahmed Ali")
           print("Profile:", result['profile'])
           print("Context:", result['context'])
           print("Phishing Message:", result['message'])
           print("Risk Analysis:", result['risk'])
