# pylint: disable=all
from openai import AzureOpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()


# Access the API key
api_key = os.getenv('DAMAI')
deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']
endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

print(api_key)  # This should print your API key
print(deployment)  # This should print your deployment key
print(endpoint)  # This should print your deployment key


# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=api_key,  # Use the variable instead of accessing os.environ again
    azure_endpoint=endpoint,
    api_version = "2024-08-01-preview"
  )

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 1.5)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.