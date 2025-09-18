# 代码生成时间: 2025-09-18 19:21:56
# Import required modules
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.clock import Clock

# Define the MathCalculator class
class MathCalculator(BoxLayout):
    result = StringProperty('0')

    def evaluate_expression(self):
        """Evaluates the mathematical expression entered by the user."""
        try:
            expression = self.ids['input_box'].text
            result = eval(expression)
            self.result = str(result)
        except Exception as e:
            # Show an error popup if the expression is invalid
            self.show_error_popup("Invalid expression: {}".format(str(e)))

    def show_error_popup(self, message):
        """Displays an error message in a popup."""
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# Define the MathCalculatorScreen class
class MathCalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(MathCalculatorScreen, self).__init__(**kwargs)
        self.manager = ScreenManager()
        self.manager.add_widget(MathCalculator())
        self.add_widget(self.manager)

# Define the MathCalculatorApp class
class MathCalculatorApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MathCalculatorScreen(name='home'))
        return screen_manager

# Run the application
if __name__ == '__main__':
    MathCalculatorApp().run()