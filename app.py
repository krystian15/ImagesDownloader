import sys
import time
import urllib.request
import random
from typing import Dict, Union


start = time.time()

flags_resolver: Dict[str, str] = {
    '-u': 'random_url',
    '-p': 'prefix',
    '-c': 'count',
    '-h': 'height',
    '-w': 'width',
    '-s': 'size',
    '-d': 'destination'
}


class ImagesDownloader:
    settings: Dict[str, Union[str, int]]

    def __init__(self):
        self.settings = {
            'images_random_url': 'https://source.unsplash.com/random',
            'images_prefix': 'image',
            'images_count': 1,
            'images_width': 800,
            'images_height': 600,
            'images_destination': '.',
            'images_terms': ['nature', 'water', 'drink', 'boots', 'sky']
        }

        self.arguments_setter()
        self.download_images()

    def arguments_setter(self):
        arguments = sys.argv

        for index, argument in enumerate(arguments):
            method_name = flags_resolver.get(argument, False)

            if method_name:
                try:
                    next_argument = arguments[(index + 1)]
                    self.settings[f'images_{method_name}'] = next_argument
                except IndexError:
                    print('Missed value for flag')

            pass

    def download_images(self):
        for count in range(0, int(self.settings.get('images_count'))):
            width: int = int(self.settings.get('images_width'))
            height: int = int(self.settings.get('images_height'))
            images_random_url: str = str(self.settings.get('images_random_url'))
            images_terms: str = random.choice(self.settings.get('images_terms'))

            url: str = f"{images_random_url}/{width}x{height}/?{images_terms}"

            urllib.request.urlretrieve(url,
                                       f"{self.settings.get('images_destination')}/"
                                       f"{self.settings.get('images_prefix')}_{count}.jpg")


ImagesDownloader()
end = time.time()

print(f'Downloaded time: {end - start}')
