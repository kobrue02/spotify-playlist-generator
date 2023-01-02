import spotipy

from keys import *


spot = spotipy.Spotify(auth_manager=token)


def create_playlist(name_of_playlist: str, desc: str):

    spot.user_playlist_create(user=username,
                              name=name_of_playlist,
                              public=True,
                              description=desc)


def add_songs_to_playlist(songs: list):
    list_of_songs = []
    for song in songs:
        result = spot.search(q=song)
        uri = result['tracks']['items'][0]['uri']
        list_of_songs.append(uri)

    playlist = spot.user_playlists(user=username)['items'][0]['id']

    spot.user_playlist_add_tracks(user=username,
                                  playlist_id=playlist,
                                  tracks=list_of_songs)


def list_of_songs_by_genre(genres: list):
    recs = spot.recommendations(seed_genres=genres)
    song_list = []
    for track in recs['tracks']:
        song_list.append(track['name'])
    return song_list


def generate_playlist(playlist_title: str, playlist_description: str, genres: list):
    create_playlist(playlist_title, playlist_description)
    songs = list_of_songs_by_genre(genres)
    add_songs_to_playlist(songs)


def main(genres):
    title = " ".join(genres)
    desc = 'automatically created'
    generate_playlist(title, desc, genres)


list_of_genres = spot.recommendation_genre_seeds()['genres']



