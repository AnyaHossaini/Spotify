'''
Take a playlist and print the songs thats it... 

1. Get to the playlist -- Print out the name of the playlist ( DONE )
2. Read the playlist (Done)
3. Print out the track name of each item on the playlist (Done)

'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def main():

    # Figure out how to call this from env file
    CLIENT_ID = "b5e6db3ad1fc4d8e9af48447b3f14924"
    CLIENT_SECRET = 


    # Processing credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist_id = 'spotify:playlist:7yHbWypQOtJaQNokIsWDdI' #URI
    playlistName(sp,playlist_id)

def playlistName(sp,playlist_id):

    playlist = sp.playlist(playlist_id)
   # print(playlist) 
    trackList(sp,playlist_id)

def trackList(sp,playlist_id):

    tracks = sp.playlist_tracks(playlist_id)

    # Print out track list in order of the playlist
    for item in tracks['items']:
        track = item['track']
        print(track['name'])

main()







