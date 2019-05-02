# client.py

import requests, os
from warrant import Cognito
from dotenv import load_dotenv
from os.path import join, dirname

class Client:

    def __init__(self): 

        # AWS cognito account info imported from .env
        dotenv_path = join(dirname(__file__), '.client_env')
        load_dotenv(dotenv_path)
        self.region = os.environ.get('REGION')
        self.userpool_id = os.environ.get('USERPOOL_ID')
        self.app_id_client = os.environ.get('APP_CLIENT_ID')
        self.app_client_secret = os.environ.get('APP_CLIENT_SECRET')
        self.username = os.environ.get('USERNAME')
        self.password = os.environ.get('PASS')

        self.user = Cognito(self.userpool_id, 
                       self.app_id_client, 
                       client_secret=self.app_client_secret, 
                       username=self.username)
        try:
            self.user.authenticate(password=self.password)
        except Exception as e:
            print(e)


    def public_api_route(self):
        response = requests.get("http://localhost:5000/public")
        return response.text


    def private_api_route(self):
        header = {}
        try:
            self.user.check_token()
            header = {"Authorization":f"Bearer {self.user.access_token}"}
        except AttributeError as e:
            print(e)
        response = requests.get("http://localhost:5000/private", headers=header) 
        return response.text


if __name__=="__main__":
    c = Client()

    print(c.public_api_route())
    print(c.private_api_route())