import requests
import json

# Define the API key and endpoint
API_KEY = 'AIzaSyBT6z1pUVoiKS0iTrWw0lMLrDhpJIp3Pus'
API_ENDPOINT = 'https://api.openai.com/v1/completions'

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Define the prompts
prompts = {
    'few_shot': {
        "prompt": "Translate the following English text to French: 'Hello, how are you?'",
        "model": "text-davinci-002",
        "temperature": 0.5,
        "max_tokens": 60
    },
    'chain_of_thought': {
        "prompt": "Q: What is the capital of France? A: Let's think it through. France is a country in Europe. The capital of a country is where its government is based. The capital of France is Paris.",
        "model": "text-davinci-002",
        "temperature": 0.5,
        "max_tokens": 60
    },
    'prompt_chain': {
        "prompt": "Step 1: Determine the largest country in the world by area. Step 2: It's Russia.",
        "model": "text-davinci-002",
        "temperature": 0.5,
        "max_tokens": 60
    },
    'fine_tuning': {
        "prompt": "Rewrite the following sentence in a more formal tone: 'Hey, wanna grab coffee tomorrow?'",
        "model": "text-davinci-002",
        "temperature": 0.5,
        "max_tokens": 60
    }
}

# Function to send the prompt to the Gemini API and print the response
def send_prompt(prompt_data):
    response = requests.post(API_ENDPOINT, headers=headers, json=prompt_data)
    if response.status_code == 200:
        print("Prompt:", prompt_data['prompt'])
        print("Response:", response.json()['choices'][0]['text'])
        print("\n-------------------------\n")
    else:
        print("Failed to fetch response:", response.status_code, response.text)

# Send each prompt and handle responses
def main():
    for key, value in prompts.items():
        print(f"Sending {key} prompt...")
        send_prompt(value)

if __name__ == '__main__':
    main()