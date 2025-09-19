# 代码生成时间: 2025-09-19 20:17:49
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random


class SortingApp(App):
    """
    A Kivy application that demonstrates sorting algorithms.
    """
    def build(self):
        # Create a BoxLayout to hold all the widgets
        layout = BoxLayout(orientation='vertical', spacing=10, padding=30)

        # Create a text input for the user to enter a list of numbers
        self.number_input = TextInput(
            text='',
            hint_text='Enter numbers separated by spaces',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.number_input)

        # Create a button to sort the numbers using the selected algorithm
        sort_button = Button(text='Sort')
        sort_button.bind(on_press=self.sort_numbers)
        layout.add_widget(sort_button)

        # Create a label to display the sorted numbers
        self.result_label = Label(text='Sorted list will appear here')
        layout.add_widget(self.result_label)

        # Set the size of the window
        Window.size = (400, 300)

        return layout

    def sort_numbers(self, instance):
        """
        Sorts the numbers entered by the user and updates the result label.
        """
        try:
            # Split the input string into a list of numbers
            numbers = [int(num) for num in self.number_input.text.split()]
            # Sort the numbers using a simple selection sort algorithm
            for i in range(len(numbers)):
                min_index = i
                for j in range(i+1, len(numbers)):
                    if numbers[j] < numbers[min_index]:
                        min_index = j
                # Swap the numbers at the current index and the minimum index
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            # Update the result label with the sorted numbers
            self.result_label.text = ' '.join(map(str, numbers))
        except ValueError:
            # Handle the error if the input is not a list of numbers
            self.result_label.text = 'Please enter a valid list of numbers'
        except Exception as e:
            # Handle any other unexpected errors
            self.result_label.text = f'An error occurred: {str(e)}'

if __name__ == '__main__':
    SortingApp().run()