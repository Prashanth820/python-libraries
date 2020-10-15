'''
Touch Input/Mouse Input
'''

'''
To handle input from the user will will create a new class called Touch.
This class will inherit from Widget and be responsible for holding our widgets and GUI elements and for handling input from the user.

Inside this touch class we will override 3 methods from the Widget class that do the following.

on_touch_down: Is triggered when the user first presses on the screen.

on_touch_up: Is triggered when the user releases the mouse or moves their finger off the screen.

on_touch_move Is triggered when the user is touching the screen and moving their finger or mouse.

'''

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5  # Change Opacity to 50%

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse UP", touch)
        self.btn.opacity = 1   # Change Opacity back to 100%



class My3App(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    My3App().run()