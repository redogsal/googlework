"""A video player class."""

from .video_library import VideoLibrary
import random
from .video_playlist import Playlist
from hashlib import new

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos: ")
        keys = list(self._video_library._videos.keys())
        keys.sort()
        for key in keys:
            current_video = self._video_library.get_video(key)
            tags = " ".join(current_video.tags)
            print("{} ({}) [{}]".format(current_video.title,current_video.video_id,tags))     
      
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videos = list(self._video_library._videos.keys())
        if video_id in videos:
            current_video = self._video_library.get_video(video_id)
            current_title = current_video.title
            if self._video_library._playing_video != "":
                print("Stopping video: {}".format(self._video_library._playing_video))
                print("Playing video: {}".format(current_title))
                self._video_library._playing_video = current_title
                self._video_library._video_id = current_video.video_id
                self._video_library._video_tags = " ".join(current_video.tags)
                self._video_library._paused = False
                
            elif current_video != self._video_library._playing_video:
                print("Playing video: {}".format(current_title))
                self._video_library._playing_video = current_title
                self._video_library._video_id = current_video.video_id
                self._video_library._video_tags = " ".join(current_video.tags)
                self._video_library._paused = False
        
        else:
             print("Cannot play video: Video does not exist")
             
   
    def stop_video(self):
        if self._video_library._playing_video == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {}".format(self._video_library._playing_video))
            self._video_library._playing_video = ""
            self._video_library._paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = list(self._video_library._videos.keys())
        if self._video_library._playing_video != "":
            print("Stopping video: {}".format(self._video_library._playing_video))
            new_video = random.choice(videos)
            new_video = self._video_library.get_video(new_video)
            new_title = new_video.title
            print("Playing video: {}".format(new_title))
            self._video_library._playing_video = new_title
            self._video_library._video_id = new_video.video_id
            self._video_library._video_tags = " ".join(new_video.tags)
            self._video_library._paused = False
        else:
            new_video = random.choice(videos)
            new_video = self._video_library.get_video(new_video)
            new_title = new_video.title
            print("Playing video: {}".format(new_title))
            self._video_library._playing_video = new_title
            self._video_library._video_id = new_video.video_id
            self._video_library._video_tags = " ".join(new_video.tags)
            self._video_library._paused = False

    def pause_video(self):
        """Pauses the current video."""
        if self._video_library._playing_video == "":
            print("Cannot pause video: No video is currently playing")
            
        elif self._video_library._playing_video != "" and self._video_library._paused == False:
            print("Pausing video: {}".format(self._video_library._playing_video))
            self._video_library._paused = True
            
        elif self._video_library._playing_video != "" and self._video_library._paused == True:
            print("Video already paused: {}".format(self._video_library._playing_video))
    
    def continue_video(self):
        """Resumes playing the current video."""
        if self._video_library._playing_video == "":
            print("Cannot continue video: No video is currently playing")
        elif self._video_library._playing_video != "" and self._video_library._paused == False:
            print("Cannot continue video: Video is not paused")
            
        elif self._video_library._playing_video != "" and self._video_library._paused == True:
            print("Continuing video: {}".format(self._video_library._playing_video))
            self._video_library._paused = False

    def show_playing(self):
        """Displays video currently playing."""
        if self._video_library._playing_video == "":
            print("No video is currently playing")
            
        elif self._video_library._playing_video != "" and self._video_library._paused == False:
            print("Currently playing: {} ({}) [{}]".format(self._video_library._playing_video, self._video_library._video_id, self._video_library._video_tags))

        elif self._video_library._playing_video != "" and self._video_library._paused == True:
            print("Currently playing: {} ({}) [{}] - PAUSED".format(self._video_library._playing_video, self._video_library._video_id, self._video_library._video_tags))
            
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        new_playlist_id = playlist_name.lower()
        if new_playlist_id in self.playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        new_playlist = Playlist(playlist_name)
        self.playlists[new_playlist_id] = new_playlist
        print("Successfully created new playlist: {}".format(playlist_name))

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_id = playlist_name.lower()
        if not playlist_id in self.playlists.keys():
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
            return
        if not self._video_library.get_video(video_id):
            print("Cannot add video to {}: Video does not exist".format(playlist_name))
            return
        if video_id in self.playlists[playlist_id].videos:
            print("Cannot add video to {}: Video already added".format(playlist_name))
            return

        video = self._video_library.get_video(video_id)
        self.playlists[playlist_id].videos.append(video_id)
        print("Added video to {}: {}".format(playlist_name, video.title))
        return
    
    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playlists.keys()) == 0:
            print("No playlists exist yet")
            return
        
        all_playlists = self.playlists.keys()
        sorted_playlists = sorted(all_playlists)

        print("Showing all playlists: ")
        for playlist in sorted_playlists:
            print(self.playlists[playlist].name)
        
        

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_id = playlist_name.lower()
        if not playlist_id in self.playlists.keys():
            print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))
            return

        playlist = self.playlists.get(playlist_id)
        videos = playlist.videos

        if len(videos) == 0:
            print("Showing playlist: {}".format(playlist_name))
            print("No videos here yet")
            return

        print("Showing playlist: {}".format(playlist_name))

        for video_id in videos:
            print(self._video_library.get_video(video_id))
           
    def remove_from_playlist(self, playlist_name, video_id):

        playlist_id = playlist_name.lower()
        if not playlist_id in self.playlists.keys():
            print("Cannot remove video from {}: Playlist does not exist".format(playlist_name))
            return
        
        if not self._video_library.get_video(video_id):
            print("Cannot remove video from {}: Video does not exist".format(playlist_name))
            return
        
        if not video_id in self.playlists[playlist_id].videos:
            print("Cannot remove video from {}: Video is not in playlist".format(playlist_name))
            return
        
        video = self._video_library.get_video(video_id)

        self.playlists[playlist_id].videos.remove(video_id)
        print("Removed video from {}: {}".format(playlist_name,video.title))
        return

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_id = playlist_name.lower()
        if not playlist_id in self.playlists.keys():
            print("Cannot clear playlist {}: Playlist does not exist".format(playlist_name))
            return

        self.playlists.get(playlist_id).videos = []
        print("Successfully removed all videos from {}".format(playlist_name))

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_id = playlist_name.lower()
        if not playlist_id in self.playlists.keys():
            print("Cannot delete playlist {}: Playlist does not exist".format(playlist_name))
            return
        
        self.playlists.pop(playlist_id)
        print("Deleted playlist: {}".format(playlist_name))

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x:x.title)
        matching_videos = []

        for video in all_videos:
            if search_term.lower() in video.title.lower():
                matching_videos.append(video)
                
        matching_videos.sort(key=lambda x:x.title)

        if len(matching_videos) == 0:
            print("No search results for {}".format(search_term))
            return

        print("Here are the results for {}".format(search_term))
        for i, matching_video in enumerate(matching_videos):
            print("{} {}".format((i+1), str(matching_video)))
        
        print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
        video_number = input()

        try:
            int_video_number = int(video_number)
            if int_video_number > len(matching_videos) or int_video_number < 0:
                return
            else:
                self.play_video(matching_videos[int_video_number - 1].video_id)
                
        except ValueError:
            return


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
