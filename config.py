##THIS IS TO LOAD THE OPEN AI API FROM ENVIRONMENT VARIABLES##
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')