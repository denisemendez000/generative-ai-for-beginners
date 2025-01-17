from openai import AzureOpenAI
import os
import requests
from PIL import Image
import dotenv
import json

# import dotenv
dotenv.load_dotenv()



#client = AzureOpenAI(
#    api_version="2024-05-01-preview",
#    azure_endpoint="https://damailearning.openai.azure.com/",
#    api_key=os.getenv('DAMAI'),  # Use the variable instead of accessing os.environ again
#)
#
#result = client.images.generate(
#    model="dall-e-2", # the name of your DALL-E 3 deployment
#    prompt="USER_PROMPT_GOES_HERE",
#    n=1
#)

# input("pause")

model = os.environ['AZURE_OPENAI_IMAGES_DEPLOYMENT']
endpoint = os.getenv('AZURE_OPENAI_IMAGES_ENDPOINT')
version = os.getenv('AZURE_OPENAI_IMAGES_VERSION')
version = "2024-05-01-preview"
api_key=os.getenv('DAMAI')
endpoint="https://damailearning.openai.azure.com/"
print(model)
print(endpoint)
print(version)

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
client = AzureOpenAI(
    api_key=os.getenv('DAMAI'),  # Use the variable instead of accessing os.environ again
    azure_endpoint=endpoint,
    api_version = version, 
  )

print("Client set")

try:
    # Create an image by using the image generation API

    result = client.images.generate(
        model=model,
        prompt='Cat riding a dragon with the logo, holding a lollipop, on a winter sky with a chat box saying meow"',    # Enter your prompt text here
        size='512x512',
        n=1
    )

    print("result generate ")
    generation_response = json.loads(result.model_dump_json())
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    print("url:", image_url)
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

    print("shoewed", image_path)
    print(model)
    print(client._api_version)

    result = client.images.generate(
    model=model,
    prompt='they say "ribbet"',    # Enter your prompt text here
    size='512x512',
    n=1
    )
    
    print("result generate 2")
    generation_response = json.loads(result.model_dump_json())
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image2.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    print("url:", image_url)
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    result = client.images.generate(
    model=model,
    prompt='foggy meadow where it grows daffodils. It says "yyyyyoooooo"',    # Enter your prompt text here
    size='512x512',
    n=1
    )

    print("result generate 3")
    generation_response = json.loads(result.model_dump_json())
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image3.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    print("url:", image_url)
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)
##########################################
###########################################
    ## not supported in azure openai
    #response = client.images.create_variation(
    #image=open(image_path, "rb"),
    #n=1,
    #size="512x512"
    #)
# catch exceptions
#except client.error.InvalidRequestError as err:
#    print(err)

finally:
    print("completed!")#
# ---creating variation below---


#
