# api.py
# This is where resources are held.
# Runs on localhost:5001

from flask import Flask, request, jsonify
import json
import auth

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home(): 
    return jsonify({
        "methods": {
            "/public": "Public route, no auth required.",
            "/private": "Private route, requires access_token in header.",
        }})

@app.route('/public', methods=['GET', 'POST'])
def public():
    return jsonify({"You are in the public route.": "Success"})

@app.route('/private', methods=['GET', 'POST'])
@auth.required
def private():
    return jsonify({"You are in the private route.": "Success"})

"""
Send post with access token in header:
curl -X POST http://localhost:5000/submit -H 'Authorization: Bearer <token>' -F data='{"key":"value"}'
"""

