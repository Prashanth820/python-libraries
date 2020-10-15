'''
Labels, Inputs and GUI Layouts
'''

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    '''
    This class will inherit from the class GridLayout (that we imported above). This will allow us to use all of the functionality of the GridLayout module created for us by kivy.
    When we inherit from GridLayout we need to call it's constructor. To do this we call super().__init__() passing in a few arguments.
    '''

    # We use **kwargs because we don't know how many arguments we may receive.
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        '''
        Adding Elements
        '''
        self.cols = 2  # We define the amount of columns to be 2
        self.add_widget(Label(text="Name: "))  # Add a label widget
        self.name = TextInput(multiline=False)  # Create a Text input box stored in the name variable
        self.add_widget(self.name)  # Add the text input widget to the GUI

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

class MyApp(App):
    def build(self):
       return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()