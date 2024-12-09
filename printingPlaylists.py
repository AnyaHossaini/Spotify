'''
Take a playlist and print the songs thats it... 

1. Get to the playlist -- Print out the name of the playlist ( DONE )
2. Read the playlist (Done)
3. Print out the track name of each item on the playlist (Done)
4. Have featured artist names be printed on the same line getting rid of duplicates
5. Print out how many times ive listended to the song 

6. Create another file (class) to read in multple playlist_ids and have them print out

'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os
from dotenv import load_dotenv

# After using Spotify's webAPI place your Client ID and Client Secret in the fields followed by all the 
# credentials needed then go and print the playlist
def main():

    # Figure out how to call this from env file
    CLIENT_ID = "b5e6db3ad1fc4d8e9af48447b3f14924"
    CLIENT_SECRET = 

    # Processing credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Capture URI
    playlist_id = 'spotify:playlist:7yHbWypQOtJaQNokIsWDdI'

    # Go to PlaylistName function
    playlistName(sp,playlist_id)

def playlistName(sp,playlist_id):

    # Get playlist name from the URI
    playlist = sp.playlist(playlist_id)

    # Print the playlist name
    print('Playlist: ' + playlist['name']) 
    print('\n')

    # Move to tracklist
    trackAndArtist(sp,playlist_id)

def trackAndArtist(sp,playlist_id):

    # Get trackList from URI
    tracks = sp.playlist_tracks(playlist_id)
   
    # Print out track list & artists in order of the playlist
    for item in tracks['items']:
        track = item['track']
        for artist in track['artists']:
            # If artist for track > 1 print artists together else: 
            print(artist['name'],track['name'])
            print('\n')

main()