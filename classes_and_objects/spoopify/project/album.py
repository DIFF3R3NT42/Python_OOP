from typing import List

from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published: bool = False
        self.songs: List[Song] = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single."
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_to_remove = None
        for song in self.songs:
            if song.name == song_name:
                song_to_remove = song
                break

        if song_to_remove is None:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song_to_remove)
        return f"Removed {song_name} from the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_info = f"Album {self.name}"
        songs_info = "\n".join([f" == {song.get_info()}" for song in self.songs])
        return f"{album_info}\n{songs_info}"

        