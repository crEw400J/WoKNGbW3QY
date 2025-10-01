# 代码生成时间: 2025-10-01 16:07:55
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.logger import Logger
from kivy.uix.label import Label

"""
Sound Manager Kivy App

This app allows users to play and manage sounds.
"""

class SoundManagerApp(App):
    def build(self):
        # Initialize the main layout
        self.sound_manager = SoundManagerLayout()
        return self.sound_manager

    def on_stop(self):
        # Stop all sounds when the app is closed
        self.sound_manager.stop_all_sounds()
        super().on_stop()

class SoundManagerLayout(BoxLayout):
    selected_sound = StringProperty()
    sounds = []
    current_sound = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.load_sounds()

    def load_sounds(self):
        """
        Load available sounds from the 'sounds' directory
        """
        try:
            self.sounds = SoundLoader.load_all('sounds')
        except Exception as e:
            Logger.error(f'Error loading sounds: {e}')

    def play_sound(self, sound_name):
        """
        Play the selected sound
        """
        if sound_name in self.sounds:
            self.stop_current_sound()
            self.current_sound = self.sounds[sound_name]
            self.current_sound.play()
            self.selected_sound = sound_name
        else:
            Logger.error(f'Sound {sound_name} not found')

    def stop_current_sound(self):
        "