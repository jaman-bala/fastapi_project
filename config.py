from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

SECRET = os.environ.get('SECRET')