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
persona = input("Tell me the historical character I want to be: ")
conversation_history = []  # Initialize an empty list to store the conversation history

count = 0  # Initialize a counter variable

while count < 5:  # Condition for the loop to run
    print("The count is:", count)  # Print the current value of count
    count += 1  # Increment the counter by 1

    question = input("Ask your question about the historical character: ")
    conversation_history.append({"role": "user", "content": question})

    prompt = f"""
    You are going to play as a historical character {persona}. 

    Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond with accurate answers only. Do not create content yourself. If you don't know something, say that you don't remember.

    Here is the conversation so far:
    {conversation_history}

    Provide an answer for the question: {question}
    """
    messages = [{"role": "user", "content": prompt}]  
    # make completion
    completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0)

    # Print response
    response = completion.choices[0].message.content
    print(response)

        # Add the model's response to the conversation history
    conversation_history.append({"role": "assistant", "content": response})

    #  very unhappy _____.

    # Once upon a time there was a very unhappy mermaid.