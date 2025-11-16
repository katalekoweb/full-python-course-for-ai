import os
from dotenv import load_dotenv

# lOad .env file
load_dotenv(".env")

# Read from enviroment
api_key = os.environ.get("API_KEY")
database = os.environ.get('DATABASE_NAME', 'default.db')
debug = os.environ.get('DEBUG')

print(f"Using database: {database}")
print(f"Using api key: {api_key}")
print(f"Debug mode: {debug}")