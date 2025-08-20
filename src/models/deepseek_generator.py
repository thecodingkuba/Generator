import os
from utils.api import AIClient, scrape_url

def call_model(prompt):
    """Call deepseek API with input prompt and returns the response"""
    os.environ["DEEPSEEK_API_KEY"] = "msk-68a74a8195300e232b449a651964efdf65ccc31f2a2e16e8f7994ae781337e01"
    client = AIClient()
    response = client.generate(prompt)
    return response

def create_solution(task):
    print(task)

def main():
    """Test main that calls the model with a simple prompt"""
    prompt = "How do I make sushi?"
    call_model(prompt)
    
if __name__ == "__main__":
    main()