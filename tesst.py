from utils import music_finder
from utils.music_finder import MusicFinder
from utils.extractor import Data
import config

config.SPOTIFY = True
config.APPLE_MUSIC = False
music = MusicFinder('True','https://github.com/abdimk/Tuneln/raw/main/test.m4a')
music_data = Data(music.finder())
#print(music_data.result())
print(music_data.SPOTIFY())
