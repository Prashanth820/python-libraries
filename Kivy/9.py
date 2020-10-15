'''
Navigation between multiple screens
'''

'''
Kivy has something called a builder that allows us to directly load any kv file that we would like. 
This allows us to avoid using the strange naming conventions that we had to follow before.
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


kv = Builder.load_file("my.kv")


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
