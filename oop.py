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

class Genre:
    def __init__(self, name):
        self.collection_genres = []
        self.name = name


    def add_subgenre(self, subgenre):
        self.collection_genres.append(subgenre)

class Genre_collection:
    def __init__(self):
        self.genre_collections = []

    def add_genre(self, genre):
        self.genre_collections.append(genre)

    def add_subgenre(self, genre):
        self.collection_genres.append(genre)


class Playlist:
    def __init__(self, name):
        self.playlist = []
        self.name = name
    
        
    


class Playlist_collection:
    def __init__(self):
        self.playlists = []

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
    
    def get_size_of_playlist_collection(self):
        return len(self.playlists)


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




