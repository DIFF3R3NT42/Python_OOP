from project.song import Song


class Album:
    def __init__(self, name: str, song: Song):
        self.name = name
        self.published: bool = False
        self.songs: list = []
        self.song = song

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)

    def remove_song(self, song_name: str):
        if song_name not in self.songs:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song_name)

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_info = f"Album {self.name}"
        songs_info = "\n".join([f" == {song.get_info()}" for song in self.songs])
        return f"{album_info}\n{songs_info}"

        