
import webbrowser
class Movie():
    def __init__(self,movie_title,movie_storyline,movie_posterimage,movie_youtubetrailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_posterimage
        self.trailer_youtube_url = movie_youtubetrailer
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
