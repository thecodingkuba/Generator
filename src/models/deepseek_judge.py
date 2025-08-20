import os
from utils.api import AIClient, scrape_url

# Test the AIClient with Deepseek
def call_model(prompt):
    # Set your API key directly
    os.environ["DEEPSEEK_API_KEY"] = "msk-68a74a8195300e232b449a651964efdf65ccc31f2a2e16e8f7994ae781337e01"
    
    # Or use the default from the API (which may be set in the file)
    client = AIClient()
    
    # Simple test prompt
    response = client.generate(prompt)
    print("AI response:", response)


def main():
    prompt = "egghead on that beat"
    call_model(prompt)

if __name__ == "__main__":
    main()