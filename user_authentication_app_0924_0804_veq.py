# 代码生成时间: 2025-09-24 08:04:56
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
import json

class UserAuthApp(App):
    """Kivy application for user authentication."""
    def build(self):
        self.title = 'User Authentication App'
        Window.size = (300, 200)
        self.root = BoxLayout(orientation='vertical')
        self.root.add_widget(Label(text='Username:'))
        self.username_input = TextInput(multiline=False)
        self.root.add_widget(self.username_input)
        self.root.add_widget(Label(text='Password:'))
        self.password_input = TextInput(password=True, multiline=False)
        self.root.add_widget(self.password_input)
        login_button = Button(text='Login')
        login_button.bind(on_press=self.login)
        self.root.add_widget(login_button)
        return self.root
    
    def login(self, instance):
        """Handle user login attempt."""
        username = self.username_input.text
        password = self.password_input.text
        if self.authenticate_user(username, password):
            self.show_popup(text='Login Successful!')
        else:
            self.show_popup(text='Login Failed!')
    
    def authenticate_user(self, username, password):
        """Authenticate the user against hardcoded credentials for demonstration purposes."""
        # In a real-world scenario, you would check the credentials against a database or an authentication service.
        valid_username = 'admin'
        valid_password = 'password123'
        return username == valid_username and password == valid_password
    
    def show_popup(self, text):
        """Display a popup with the given text."""
        popup = Popup(title='Message', content=Label(text=text), size_hint=(None, None), size=(200, 200))
        popup.open()

if __name__ == '__main__':
    UserAuthApp().run()