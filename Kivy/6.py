'''
The Float Layout for dynamic placements
'''

'''
A FloatLayout allows us to place elements using something called a relative position.
This means that rather than defining specific coordinates we will place everything 
using percentages or based on the current window width and height. This way when we 
change the window dimensions everything we have placed will adjust size and position 
accordingly making our application scale to the size of the window.
'''

'''The two properties we will use to create a dynamic placement are:

- pos_hint

- size_hint

Note 1: You can only use values between 0-1 for both size_hint and pos_hint. Where 0 = 0% and 1 = 100%.

Note 2: The coordinate system  in kivy works from the bottom left! This will be important when placing our objects.

To create a dynamic size for our buttons we will set the size_hint for each of our buttons to be 0.5, 0.5 . 
This will make each of our buttons take up 50% width and 50% height of the container they are in.

When creating a dynamic position we can define up to 6 keys in a dictionary like so:
pos_hint = {"x":1, "y":1, "left":1, "right":1, "top":1, "bottom":1}'''

import kivy
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout

class My2App(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    My2App().run()