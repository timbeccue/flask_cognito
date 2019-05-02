# Flask_Cognito

This is intended to be a simplest-possible demonstration of aws cognito-based authentication in a flask api. Communication between Cognito and python uses [warrant](https://github.com/capless/warrant).

The flask application depends on a `.api_env` file to read the cognito user pool details. The client similiarly depends on `.client_env`. These dotfiles load the enviornment variables that are imported in auth.py and client.py--refer to these files for the details.

To start the api, install the dependencies in requirements.txt and type `$ flask run`. That should create a local server at http://localhost:5000.

You can interact with this server in the usual manner, or with the premade client in `client.py`. Simply run the `$ python client.py` to test both the public and private api endpoints. Or modify the client class as you wish. 