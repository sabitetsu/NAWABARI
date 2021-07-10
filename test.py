#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label

class Test(App):
    def build(self):
        return Label(text='Hello World')

Test().run()
