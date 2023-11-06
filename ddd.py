import nltk
from nltk_utils import *
import webbrowser
from webbrowser import *
import threading
text=input()
li=tokenize(text)
print(li)
if "happy" in li:
    spotify_link = "https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD"
def dev():
    w = webbrowser.open_new(spotify_link)

# Schedule the function to be called in 2 seconds
t = threading.Timer(10.0, dev)
t.start()
