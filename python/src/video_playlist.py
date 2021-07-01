"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, original_name: str):
    
        self._playlist_name = original_name
        self._reference = original_name.lower()
        self.videos = []
        

    @property
    def name(self) -> str:
        """Returns the name of the playlist."""
        return self._playlist_name

    @property
    def reference(self) -> str:
        """Returns the reference name of the playlist i.e. uppercase version."""
        
