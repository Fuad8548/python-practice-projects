# Python practice project covering dunder methods
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
 
    def __repr__(self):
        return f"Song({self.title!r}, {self.artist!r})"
 
    def __str__(self):
        return f"{self.title} — {self.artist}"
 
    def __eq__(self, other):
        if not isinstance(other, Song):
            return NotImplemented
        return (self.title, self.artist) == (other.title, other.artist)
 
    def __hash__(self):
        # in case Songs are ever put in a set/dict.
        return hash((self.title, self.artist))

class MusicLibrary:
    def __init__(self):
        self._songs = []
 
    # -- regular methods ==================
    def add(self, song):
        self._songs.append(song)
 
    def remove(self, song):
        self._songs.remove(song)
 
    def list_items(self):
        return list(self._songs)
 
    # -- dunder methods ====================
    def __len__(self): 
        return len(self._songs)
 
    def __getitem__(self, index):
        # library[0], library[1:3]
        return self._songs[index]
 
    def __contains__(self, song):
        # `song in library`. Uses Song.__eq__ under the hood, so this checks by value, not identity.
        return song in self._songs
 
    def __iter__(self):
        # `for song in library:`
        # a fresh iterator each call, so two loops over the same library
        return iter(self._songs)
 
    def __repr__(self):
        return f"MusicLibrary({len(self._songs)} songs)"

# Test the methods
lib = MusicLibrary()

    print("-- add --")
    lib.add(Song("Blinding Lights", "The Weeknd"))
    lib.add(Song("Easy On Me", "Adele"))
    lib.add(Song("As It Was", "Harry Styles"))
    print(repr(lib))
 
    print("\n-- list_items --")
    for song in lib.list_items():
        print(" ", song)
 
    print("\n-- len --")
    print("len(lib):", len(lib))
 
    print("\n-- getitem --")
    print("lib[0]: ", lib[0])
    print("lib[:2]:", [str(s) for s in lib[:2]])
 
    print("\n-- contains --")
    query = Song("Easy On Me", "Adele")
    print("query in lib:", query in lib)
    print("fake in lib: ", Song("Fake Song", "Nobody") in lib)
 
    print("\n-- iter --")
    for song in lib:
        print(" ->", song)
 
    print("\n-- remove --")
    lib.remove(query)
    print("after removing 'Easy On Me':")
    print(" ", [str(s) for s in lib.list_items()])
    print("len(lib) now:", len(lib))

