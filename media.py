
import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,movie_posterimage,movie_youtubetrailer):
        #Creating class for movie that stores the information of that movie a
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_posterimage
        self.trailer_youtube_url = movie_youtubetrailer
    def show_trailer(self):
        #Function to play the trailer fo the given movie.
        webbrowser.open(self.youtube_trailer)
