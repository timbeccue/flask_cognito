# auth.py

from flask import request, jsonify
from warrant import Cognito
from warrant.exceptions import TokenVerificationException
from functools import wraps
from dotenv import load_dotenv
import os

# AWS cognito account info imported from .env
load_dotenv('.api_env')
REGION = os.environ.get('REGION')
USERPOOL_ID = os.environ.get('USERPOOL_ID')
APP_CLIENT_ID = os.environ.get('APP_CLIENT_ID')
APP_CLIENT_SECRET = os.environ.get('APP_CLIENT_SECRET')

# Object (from warrant module) used to verify access tokens. 
cognito_helper = Cognito(USERPOOL_ID, APP_CLIENT_ID, client_secret=APP_CLIENT_SECRET)

# This decorator only returns the decorated function if it has a valid 
# access token. Otherwise, it will return json with the reason for rejection.
def required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        headers = request.headers
        try:
            auth_header = headers['Authorization'] 
            access_token = auth_header.split()[-1]
            cognito_helper.verify_token(access_token, 'access_token', 'access')
            print("Token successfully verified")
            return f(*args, **kwargs)
        # In case there's no authorization header.
        except KeyError:
            print('KeyError: No authorization header value present.')
            return jsonify({"error":"No authorization header present."})
        # In case the token doesn't verify.
        except TokenVerificationException:
            print('TokenVerificationException: access token could not be verified.')
            return jsonify({"error":"Access token could not be verified."})
    return wrapped

