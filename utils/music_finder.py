'''Music Finder'''
import json
import os
import requests
import config


class MusicFinder(object):
    '''Main Class'''
    def __init__(self, return_api, music_url):
        '''object of a class is instantiated'''
        self.return_api = return_api
        self.api_token = os.environ['api_token']
        self.music_url = music_url

    def finder(self):
        '''finder method and return as json decode'''
        if (config.APPLE_MUSIC and config.SPOTIFY):
            ava = 'apple_music,spotify'
            data = {'url': f'{self.music_url}', 'return': f'{ava}',
                    'api_token': f'{self.api_token}'}
        if config.APPLE_MUSIC is True and config.SPOTIFY is False:
            ava = 'apple_music'
            data = {'url': f'{self.music_url}', 'return': f'{ava}',
                    'api_token': f'{self.api_token}'}
        if config.SPOTIFY is True and config.APPLE_MUSIC is False:
            ava = 'spotify'
            data = {'url': f'{self.music_url}', 'return': f'{ava}',
                    'api_token': f'{self.api_token}'}
        result = requests.post('https://api.audd.io/', data=data)
        music_data = json.loads(result.text)
        return music_data
