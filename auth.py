
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:65010/spotify_callback"

from flask import Flask

app = Flask(__name__)
@app.route('/')

def homepage():
    text = '<a href="%s">Authenticate with Spotify</a>'
    return text % make_authorization_url()

def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    from uuid import uuid4
    state = str(uuid4())
    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "redirect_uri": REDIRECT_URI,
              "duration": "temporary",
              "scope": "user-read-private user-read-email playlist-modify-public"}
    import urllib.parse
    url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
    return url

def is_valid_state(state):
    return True

if __name__ == '__main__':
    app.run(debug=True, port=65010)

from flask import abort, request

@app.route('/spotify_callback')
def spotify_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        abort(403)
    code = request.args.get('code')
    return "Got a token!: %s" % get_token(code)

# import requests
# import requests.auth
# def get_token(code):
#    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
#    post_data = {"grant_type": "authorization_code",
#                 "code": code,
#                 "redirect_uri": REDIRECT_URI}


from tekore.auth import Credentials

def get_token(code):
    cred = Credentials(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    user_token = cred.request_user_token(code)

    return user_token

