# 代码生成时间: 2025-09-29 00:00:25
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex

"""
Media Asset Management Application using Kivy Framework
"""

class MediaAssetManagementApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical')

        # File chooser for selecting media files
        self.file_chooser = FileChooserIconView(
            size_hint=(0.8, 0.8),
            size=(400, 400),
            filters=['*.jpg', '*.png', '*.gif', '*.mp4', '*.mov'],
            rootpath=os.getcwd()
        )
        file_chooser_scroll = ScrollView(size_hint=(1, 1))
        file_chooser_scroll.add_widget(self.file_chooser)
        main_layout.add_widget(file_chooser_scroll)

        # Add button to add media assets
        add_button = Button(text='Add Media Asset', size_hint=(1, 0.2))
        add_button.bind(on_release=self.add_media_asset)
        main_layout.add_widget(add_button)

        # Label to display messages
        self.message_label = Label(size_hint=(1, 1), text='', halign='left')
        main_layout.add_widget(self.message_label)

        return main_layout

    def add_media_asset(self, instance):
        """
        Add media asset to the application
        """
        # Get the selected media files
        selected_files = self.file_chooser.selection
        if not selected_files:
            self.show_error_popup('No media asset selected.')
            return

        # Process each selected file
        for file_path in selected_files:
            try:
                # Here you would add your logic to handle adding the
                # media asset to your asset management system
                # For demonstration, we'll just print the file path
                print(f'Adding media asset: {file_path}')
                self.message_label.text = 'Media asset added successfully.'
            except Exception as e:
                self.show_error_popup(f'Error adding media asset: {e}')
                return

    def show_error_popup(self, error_message):
        """
        Show an error popup with the given message
        """
        popup = Popup(title='Error', content=Label(text=error_message), size_hint=(0.9, 0.7))
        popup.open()


if __name__ == '__main__':
    MediaAssetManagementApp().run()
