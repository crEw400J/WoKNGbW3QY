# 代码生成时间: 2025-09-20 04:29:18
# json_converter_app.py

"""
A simple Kivy application for converting JSON data format.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import json


class JsonConverterLayout(BoxLayout):
    """
    A Kivy BoxLayout that handles the UI for the JSON Converter.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Input area
        self.json_input_layout = BoxLayout(orientation='horizontal')
        self.json_input = TextInput(multiline=True, size_hint_y=None, height=200)
        self.json_input_layout.add_widget(self.json_input)

        # Output area
        self.json_output_layout = BoxLayout(orientation='horizontal')
        self.json_output = Label(text='', size_hint_y=None, height=200, halign='left')
        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.scroll_view.add_widget(self.json_output)
        self.json_output_layout.add_widget(self.scroll_view)

        # Buttons
        self.convert_button = Button(text='Convert JSON')
        self.convert_button.bind(on_press=self.convert_json)

        # Add widgets to the layout
        self.add_widget(self.json_input_layout)
        self.add_widget(Label(text='Converted JSON:'))
        self.add_widget(self.json_output_layout)
        self.add_widget(self.convert_button)

    def convert_json(self, instance):
        """
        Convert the JSON data from the input text area to a pretty-printed format.
        """
        try:
            # Get the input JSON string
            input_json = self.json_input.text
            # Parse the JSON data
            data = json.loads(input_json)
            # Convert to a pretty-printed JSON string
            output_json = json.dumps(data, indent=4)
            # Update the output label with the pretty-printed JSON
            self.json_output.text = output_json
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            self.json_output.text = 'Invalid JSON: ' + str(e)
        except Exception as e:
            # Handle any other exception
            self.json_output.text = 'An error occurred: ' + str(e)


class JsonConverterApp(App):
    """
    The main Kivy application class for the JSON Converter.
    """
    def build(self):
        # Create an instance of the JsonConverterLayout
        return JsonConverterLayout()


if __name__ == '__main__':
    # Create and run the application
    JsonConverterApp().run()