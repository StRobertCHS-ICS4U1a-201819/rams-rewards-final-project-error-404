import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label
from kivy.core.window import Window

#
# class homepage(BoxLayout):
#
#     def Title(self):
#         return BoxLayout()


class StudentApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return BoxLayout()



sApp = StudentApp()
sApp.run()