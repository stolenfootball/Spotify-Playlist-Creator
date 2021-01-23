
import spotipy

sp = spotipy.Spotify(auth='BQDuLYE1103eIMS4cXXs_ZKvrH8APx2brnnQrcpPevqxyA4ALQ9b-r9mv4kq7sN1Iyyb9bVB0CYo5GwqO-IJgUL6U45KQ8IMCqYrw2evorTxFvxl1xKvXej8181DZgmTchTFaaWkBVZpfPHkwF71pneCNbre9sD0nLLOQrIm-ySmEf3sBiXLWO9z7mJ3PhgIqgd9pNmChmy9Wta1qqA')

username = ''

playlist_id = '2TuPYgMb6U3rDoCf4VY20E'

artist_list = ["Franz Ferdinand",
               "Better Than Ezra",
               "Jade Bird",
               "cleopatrick",
               "The Doobie Brothers",
               "Nazareth",
               "Young the Giant",
               "Social Distortion",
               "3 Doors Down",
               "Faces",
               "Muse",
               "Iggy Pop",
               "Faces",
               "Kyuss",
               "Terry Reid",
               "Taylor Hawkins & The Coattail Riders",
               "The Vines",
               "Black Rebel Motorcycle Club"]

def get_tracks(artist_name):
    artist = sp.search(artist_name, type=('artist',))
    a_id = artist['artists']['items'][0]['id']
    fin = []

    for trk in sp.artist_top_tracks(a_id)['tracks']:
        fin.append(trk['id'])

    return fin

def add_tracks_to_playlist(track_list):
    results = sp.user_playlist_add_tracks(username, playlist_id, track_list)
    return results

x = 0
for item in artist_list:
    print(item)
    fin = get_tracks(item)
    res = add_tracks_to_playlist(fin)
    print("Complete")


#playlists = sp.user_playlists(username)
#for playlist in playlists['items']:
#    if playlist['owner']['id'] == username:
#        print()
#        print(playlist['name'], playlist['id'])
