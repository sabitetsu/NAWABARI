#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class MyWidget(Widget):
    pass

class TestApp(App):

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'    # ウィンドウの名前を変更

        def build(self):
            return MyWidget()


if __name__ == '__main__':
    TestApp().run()
