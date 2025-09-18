# 代码生成时间: 2025-09-19 07:36:22
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp


class ResponsiveBoxLayout(BoxLayout):
    """
    A responsive BoxLayout that adapts to the window size.
    """
    responsive = BooleanProperty(True)
    """
    Indicates whether the layout should be responsive.
    """

    def on_size(self, instance, value):
        """
        Triggered when the size of the layout changes.
        """
        if self.responsive:
            self.adapt_layout()

    def adapt_layout(self):
        """
        Adapts the layout based on the window size.
        """
        if Window.width < 400:  # Small screen
            self.orientation = 'vertical'
        else:  # Large screen
            self.orientation = 'horizontal'

    def on_responsive(self, instance, value):
        """
        Triggered when the responsive property changes.
        """
        if value:
            self.adapt_layout()
        else:
            self.orientation = 'vertical'  # Default to vertical


class ResponsiveLayoutApp(App):
    """
    The main application class.
    """
    def build(self):
        """
        Builds the application.
        """
        layout = ResponsiveBoxLayout()
        layout.add_widget(Label(text='Hello, Kivy!', size_hint_y=None, height=dp(50)))
        layout.add_widget(Button(text='Click me', size_hint_y=None, height=dp(50)))

        # Trigger initial adaption
        layout.adapt_layout()

        return layout

    def on_pause(self):
        """
        Handle application pause.
        """
        return True


if __name__ == '__main__':
    ResponsiveLayoutApp().run()
