import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.pagelayout import PageLayout




class StudentApp(App):

    def build(self):
        return PageLayout()



sApp = StudentApp()
sApp.run()