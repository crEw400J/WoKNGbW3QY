# 代码生成时间: 2025-09-24 00:49:35
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class ShoppingCartApp(App):
    def build(self):
        sm = ScreenManager()
        screen = Screen(name='home')
        sm.add_widget(screen)
        return sm

    def on_start(self):
        self.cart = ShoppingCart()
        self.cart.bind(modified=self.update_cart_summary)
        self.update_cart_summary()

    def update_cart_summary(self, *args):
        self.root.ids.cart_summary_label.text = f"Items in cart: {len(self.cart.items)}"


class ShoppingCart(Widget):
    items = ListProperty()
    modified = ListProperty()

    def add_item(self, item):
        # Check if item is already in the cart
        if item not in self.items:
            self.items.append(item)
            self.trigger_modified()
        else:
            # If item is already in the cart, increment the count
            for i, existing_item in enumerate(self.items):
                if existing_item == item:
                    self.items[i] += 1
                    self.trigger_modified()
                    return

    def remove_item(self, item):
        # Check if item is in the cart and decrement its count
        for i, existing_item in enumerate(self.items):
            if existing_item == item:
                if self.items[i] > 1:
                    self.items[i] -= 1
                else:
                    self.items.remove(existing_item)
                self.trigger_modified()
                return
        raise ValueError("Item not found in the cart.")

    def trigger_modified(self):
        self.modified = []  # Trigger the event that the cart has been modified


class ShoppingCartScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ShoppingCartScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.cart_summary_label = Label(text='Items in cart: 0')
        self.add_widget(self.cart_summary_label)
        self.add_widget(Button(text='Add Item', on_press=self.add_item))
        self.add_widget(Button(text='Remove Item', on_press=self.remove_item))

    def add_item(self, instance):
        # Add an item to the cart (for demonstration purposes, add a fixed item)
        self.app.cart.add_item(10)

    def remove_item(self, instance):
        # Remove an item from the cart (for demonstration purposes, remove a fixed item)
        self.app.cart.remove_item(10)


class ShoppingCartItem:
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity


# Define the Kivy application
if __name__ == '__main__':
    ShoppingCartApp().run()
