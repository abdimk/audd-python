from utils import music_finder

class Data(object):
    def __init__(self, music_data):
        self.music_extracted_data = music_data

    def result(self):
        '''Total result from the api as json data'''
        return self.music_extracted_data['result']

    def artist(self):
        '''artist'''
        return self.music_extracted_data['result']['artist']

    def title(self):
        '''music title'''
        return self.music_extracted_data['result']['title']

    def album(self):
        '''album name'''
        return self.music_extracted_data['result']['album']

    def release_date(self):
        '''release_date for the music'''
        return self.music_extracted_data['result']['release_date']

    def label(self):
        '''label of the music'''
        return self.music_extracted_data['result']['label']

    def timecode(self):
        '''time code for the music'''
        return self.music_extracted_data['result']['timecode']

    def song_link(self):
        '''song link for the music in the apple music data base'''
        return self.music_extracted_data['result']['song_link']

    def apple_music(self):
        '''result for the song in the apple music Note rturn'''
        return self.music_extracted_data['result']['apple_music']

    def apple_music_previews(self):
        '''apple_music_previews'''
        return self.music_extracted_data['result']['apple_music']['previews']

    def apple_music_previews_url(self):
        '''apple_music_previews_url'''
        return self.music_extracted_data['result']['apple_music']['previews'][0]['url']

    def artwork(self):
        '''artwork'''
        return self.music_extracted_data['result']['apple_music']['artwork']

    def artistName(self):
        return self.music_extracted_data['result']['apple_music']['artistName']

    def apple_url(self):
        '''apple_url'''
        return self.music_extracted_data['result']['apple_music']['url']

    def discNumber(self):
        '''discNumber'''
        return self.music_extracted_data['result']['apple_music']['discNumber']

    def genreNames(self):
        '''genreNames'''
        return self.music_extracted_data['result']['apple_music']['genreNames']

    def durationInMillis(self):
        '''durationInMillis'''
        return self.music_extracted_data['result']['apple_music']['durationInMillis']

    def releaseDate(self):
        '''releaseDate'''
        return self.music_extracted_data['result']['apple_music']['releaseDate']

    def name(self):
        '''name'''
        return self.music_extracted_data['result']['apple_music']['name']

    def isrc(self):
        '''isrc'''
        return self.music_extracted_data['result']['apple_music']['isrc']

    def albumName(self):
        '''albumName'''
        return self.music_extracted_data['result']['apple_music']['albumName']

    def playParams(self):
        '''playParams'''
        return self.music_extracted_data['result']['apple_music']['playParams']

    def trackNumber(self):
        '''trackNumber'''
        return self.music_extracted_data['result']['apple_music']['trackNumber']

    def composerName(self):
        '''composerName'''
        return self.music_extracted_data['result']['apple_music']['composerName']

    def SPOTIFY_album_name(self):
        return self.music_extracted_data['result']['spotify']['album']['name']

    def SPOTIFY_album_artists(self):
        return self.music_extracted_data['result']['spotify']['album']['artists']

    def SPOTIFY_spotify(self):
        return self.music_extracted_data['result']['spotify']['album']['artists'][0]['external_urls']

    def SPOTIFY_album_group(self):
        return self.music_extracted_data['result']['spotify']['album']['album_group']

    def SPOTIFY(self):
        return self.music_extracted_data['result']['spotify']['album']
