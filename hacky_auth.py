from tekore.auth import Credentials

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:65010/spotify_callback"


cred = Credentials(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
user_token = cred.request_user_token('AQDFcIcVR34lVRAmr9jIoUVbUgxkLxvnZXwzntIjqODTEtqdmYxd67kyWE0n0-cNmAlW_wJ50QGhPN_efnB1ISmvJGTFmU2BlZKzobcbQWjy2d3dXhhHKpvz5eqnU4Z5W9uhIdvQMRwwELd4RVzYGvs1GR6SnOnfue2a6Dnt9fRIif8Z27qvCHxCWVT99jONQ8j_DtjZAo4zHiXpwL7t20XyUAcVGnNL3IsLLBOVhjc4XzOYVB-_Wxx1NnFz3e9Rw_wRNVvpcg')
#user_token = cred.refresh('BQCAz12Yp3z7J-1nMmtW5YKUmmV4B037yoKnYyixEHsPjdDv3bOm5oWvdTFSgWhis-1LshShWzRKp8XrGeJ_j-ylUpVfIGVQw-hTrhT8pGaAWmDoY2cLzyQNKPvrjXHslUd5ndwvMmH5iouniowCaBLH9-ucuVjSYNbScAYRZsSBr3KfAsOwbw')
print(str(user_token))