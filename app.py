import os
from langchain_google_genai import ChatGoogleGenerativeAI


# Load the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Initialize the Gemini model
llm4 = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key='AIzaSyDvFvjpe4CVEzcgIZnb-Xb3maIRX-wXZU')

# Define your query
text = "What is the capital of the USA?"


# Get the response from the model
response = llm4.predict(text)
print(response)
