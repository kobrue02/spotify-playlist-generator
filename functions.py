import json

import spotipy

from keys import *


spot = spotipy.Spotify(auth_manager=token)


def create_playlist(name_of_playlist: str, desc: str):

    spot.user_playlist_create(user=username,
                              name=name_of_playlist,
                              public=True,
                              description=desc)


def add_songs_to_playlist(songs: list):

    playlist = spot.user_playlists(user=username)['items'][0]['id']

    spot.user_playlist_add_tracks(user=username,
                                  playlist_id=playlist,
                                  tracks=songs)


def list_of_songs_by_genre(genres: list) -> list:

    query = "genre: {}".format(genres[0].replace(" ", "_"))
    if len(genres) > 1:
        for genre in genres[1:]:
            genre = genre.replace(" ", "_")
            query += " AND genre: {}".format(genre)

    recs = spot.search(q=query, type='track', limit=50, offset=0)
    songs = [track['uri'] for track in recs['tracks']['items']]
    return songs


def generate_playlist(playlist_title: str, playlist_description: str, genres: list):
    create_playlist(playlist_title, playlist_description)
    songs = list_of_songs_by_genre(genres)
    add_songs_to_playlist(songs)


def main(genres):
    title = " ".join(genres)
    desc = 'automatically created'
    generate_playlist(title, desc, genres)


list_of_genres = spot.recommendation_genre_seeds()['genres']

if __name__ == "__main__":
    genres = ['blues', 'rock']
    print(list_of_songs_by_genre(genres))



