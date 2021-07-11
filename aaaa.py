from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapview = MapView(xoom=17,lat=35.681382,lon=139.766084)#ここにつばきちの位置情報を入れたい
        return mapview

MapViewApp().run
