from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.app import App
import locationtest
class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=50, lat=35.681382, lon=139.766084)
        marker1 = MapMarkerPopup(lat=35.681382, lon=139.766084) 
        mapview.add_marker(marker1)
        return mapview

new_var = MapViewApp().run()