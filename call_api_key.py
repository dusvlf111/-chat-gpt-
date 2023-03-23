import os
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the API key from the configuration file
openai_api_key = config['OPENAI']['API_KEY']

# Set the API key as an environment variable
os.environ['OPENAI_API_KEY'] = openai_api_key
