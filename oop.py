class Song:
    def __init__(self, name, subgenre):
        self.name = name
        self.subgenre = subgenre

class Album:
    def __init__(self,  name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_size_of_album(self):
        return len(self.songs)

class Artist:
    def __init__(self, name):
        self.name = name
        self. creatures = []

    def add_album(self, album):
        self.creatures.append(album)

    def number_of_albums(self):
        return len(self.creatures)   

class Album_collection:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def size_of_album_coll(self):
        return len(self.albums)



class Playlist_collection:
    def __init__(self):
        self.playlists = []

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

name_s1 = "jojo"
subg1 = "jo"
song = Song(name_s1, subg1)
name_a1 = "hhh"
album = Album(name_a1)
album.add_song(song.name)
name_ar1 = "Reno"
artist = Artist(name_ar1)
album_collection = Album_collection()
album_collection.add_album(album)
print(song.name, album.name, album.songs[0], artist.name,
album_collection.albums[0].name)



