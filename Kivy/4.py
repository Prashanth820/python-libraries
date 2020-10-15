'''
The kv Design language
'''

'''
Kivy has something called the kv design language. 
You think of it as a language similar to HTML and 
CSS where it is responsible for styling and adding 
elements to the display but does not handle any logic. 
In this tutorial I will show you how to create a .kv 
file and create the graphical part of your application 
from within that file.
'''

'''
There are a few conventions we need to follow when creating a .kv file.

Naming: The name of your .kv file must follow the rules below in order for python/kivy to be able to see and load the file.
1. It must be all lowercase
2. It must match with the name of your main class. (The one that has the build method)
3. If the name of your main class ends in "app" (lowercase or uppercase) you must not include "app" in your file name.

File Location: The file must be in the same directory as your python script.

File Extension: The file must be saved as type *All Files and end with .kv
'''

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass


class MyApp(App): # <- Main Class
    def build(self):
        return MyGrid()
    def hello(self):
        print("hello")


if __name__ == "__main__":
    MyApp().run()