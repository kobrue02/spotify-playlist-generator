import random

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from functions import *

kivy.require('1.9.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))

    def generate_playlist(self):
        genres = ['Blues', 'Rock']
        main(genres)
        self.scs_label.text = 'Success!'


class NeuralRandom(App):

    def build(self):
        return MyRoot()


if __name__ == "__main__":
    nr = NeuralRandom()
    nr.run()

