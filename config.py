from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

# Define the API key and header name
API_KEY = getenv("API_KEY")
API_KEY_NAME = "X-API-Key"  # Header name for the API key

if API_KEY is not None:
    print("api key loaded")
