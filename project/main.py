import json
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.preprocessing import MinMaxScaler

client_id = '' # client id
client_secret = '' #client secret id

client_cred_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_cred_manager)


playlist_id = '' # enter playlist to analyze
res = sp.playlist(playlist_id)

ids = []
for item in res['tracks']['items']:
    track = item['track']['id']
    ids.append(track)

song_meta = {'id':[], 'album':[], 'name':[],
              'artist':[], 'popularity':[]}

for song_id in ids:
    meta = sp.track(song_id)

    song_meta['id'].append(song_id)

    # get album name
    album = meta['album']['name']
    song_meta['album'] += [album]

    # get song name
    song=meta['name']
    song_meta['name'] += [song]

    # get artist name
    s = ', '
    artist = s.join([singer_name['name'] for singer_name in meta['artists']])
    song_meta['artist'] += [artist]

    # song popularity
    popularity = meta['popularity']
    song_meta['popularity'].append(popularity)


song_meta_df = pd.DataFrame.from_dict(song_meta)

# song features
features = sp.audio_features(song_meta['id'])

features_df = pd.DataFrame.from_dict(features)

song_meta_df.head()