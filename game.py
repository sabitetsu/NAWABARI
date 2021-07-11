#-*- coding: utf-8 -*-
import time
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '854')

from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.clock import Clock

class Game(Widget):
    text  = StringProperty()
    color = ListProperty([1,1,1,1])
    count = 0
    startCount = 3
    ready = True
    countPhase = False
    countPhaseT = 5
    s = 0
    timingGame = False
    gauge_length = 200
    gauge = 0
    gaugeUpper = 8
    stop = False


    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.text = 'Ready...'


    def buttonClicked(self):
        if self.startCount >= 3:
            self.ready = False
            self.text = str(self.startCount)
        elif self.countPhase:
            self.count += 1
        elif self.timingGame:
            self.stop = True

    def move(self):
        self.gauge += self.gaugeUpper
        if self.gauge >= self.gauge_length:
            self.gaugeUpper = -self.gaugeUpper
        elif self.gauge <= 0:
            self.gaugeUpper = -self.gaugeUpper

    def update(self, dt):
        if self.ready:
            None
        elif self.startCount > 0:
            time.sleep(1)
            self.startCount -= 1
            self.text = str(self.startCount)
        elif self.startCount <= 0 and self.count == 0 and not(self.countPhase) and not(self.timingGame):
            self.countPhase = True
            self.s = time.time()
        elif self.countPhase:
            if self.countPhaseT <= 0:
                self.countPhase = False
                self.timingGame = True
            else:
                self.text = str(self.countPhaseT)
            if time.time() - self.s >= 1:
                self.countPhaseT -= 1
                self.s = time.time()
        elif self.timingGame:
            if self.stop:
                self.text = str(self.gauge * self.count)
            else:
                self.move()
                self.text = "■" * (1+(self.gauge//20))



class GameApp(App):

    def __init__(self, **kwargs):
        super(GameApp, self).__init__(**kwargs)
        self.title = 'Game'    # ウィンドウの名前を変更

    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    GameApp().run()
