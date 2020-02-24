#importing the module 
import pytube
from pytube import Playlist

SAVE_PATH = "C:/Downloads/" #to_do 

plist = Playlist('www.youtube.com/watch?v=SEnXr6v2ifU&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI')
#plist = Playlist('www.youtube.com/watch?v=E7_a-kB46LU&list=PLqq-6Pq4lTTbx8p2oCgcAQGQyqN8XeA1x')

plist.download_all(SAVE_PATH)
