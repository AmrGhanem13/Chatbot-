# Import the Together API client
from together import Together

# Import dotenv to load environment variables from a .env file (e.g., API keys)
from dotenv import load_dotenv

# Load environment variables from the .env file into the environment
load_dotenv()

# Initialize the Together client (uses API key from environment variables)
client = Together()

# Create a chat completion request using the LLaMA-3.3 70B instruct model
response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  # Specify the model
    messages=[
        {
            "role": "user",         # Role of the message sender
            "content": "what is the capital of USA"  # User's query to the model
        }
    ]
)

# Print the model's response from the first choice
print(response.choices[0].message.content)
