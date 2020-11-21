import time
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from plyer import gps
####### root ###########
class TheRoot(Widget):
    label = ObjectProperty(None)
####### App #############
class ShowCor(App):
    def build(self):
        return TheRoot()
    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
    def on_gps_location(self, **kwargs):
        label = ObjectProperty(None)
        lat = str(kwargs["lat"])
        lon = str(kwargs["lon"])
        self.lable.text = "lat: " + lat + "lon:" + lon
ShowCor().run()
