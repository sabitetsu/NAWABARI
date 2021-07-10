#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty

class MyWidget(Widget):
    text  = StringProperty()
    color = ListProperty([1,1,1,1])
    count = 0

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.text = 'start'

    def buttonClicked(self):
        self.count += 1
        if self.count == 1:
            self.text = 'なんで押すんだよ'
            self.color = [1, 0, 0, 1]
        elif self.count == 2:
            self.text = 'おい'
        elif self.count == 3:
            self.text = 'だから'
        elif self.count == 4:
            self.text = 'なんで'
        elif self.count == 5:
            self.text = '押すんだよ'
        elif self.count > 5:
            self.text = 'おい！！！！'

class TestApp(App):

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'    # ウィンドウの名前を変更

        def build(self):
            return MyWidget()


if __name__ == '__main__':
    TestApp().run()
