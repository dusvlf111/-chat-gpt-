import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Get question input from user
prompt = input("Ask a question: ")

# Call the OpenAI API to generate a response
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated response
print(response.choices[0].text.strip())
