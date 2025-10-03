# 代码生成时间: 2025-10-04 02:16:26
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.treeview import TreeViewLabel, TreeView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FilteredTreeview(TreeView):
    def on_touch_down(self, touch):
        # Override the default touch_down method to handle sorting by column
        if super(FilteredTreeview, self).on_touch_down(touch):
            return True
        column = self._touch_column
        if column and column[0] is True:
            # Toggle sorting by the column
            self._trigger_reset_treeview()
            self._sort_func = self._reverse_sort_func if self._sort_func else self._sort_func
            self._trigger_treeview_update()
            return True
        return False

class TableSortFilterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.filter_input = TextInput(multiline=False, size_hint_y=None, height=50)
        self.filter_button = Button(text='Filter')
        self.filter_button.bind(on_press=self.filter_data)
        self.treeview = FilteredTreeview(
            hide_root=False,
            size_hint=(1, 0.8),
            root_options=dict(text='Items'),
            columns=(('Name', '50dp'), ('Age', '50dp')),
            column_widths=('50dp', '50dp')
        )
        
        # Sample data for the table
        self.data = [
            {'Name': 'Alice', 'Age': '30'},
            {'Name': 'Bob', 'Age': '25'},
            {'Name': 'Charlie', 'Age': '35'},
            # Add more data as needed
        ]
        
        # Initialize the treeview with data
        self.populate_treeview()
        
        # Add the filter input, button, and treeview to the layout
        filter_box = BoxLayout()
        filter_box.add_widget(self.filter_input)
        filter_box.add_widget(self.filter_button)
        
        self.layout.add_widget(filter_box)
        self.layout.add_widget(self.treeview)
        return self.layout

    def populate_treeview(self):
        # Populate the treeview with the data
        for item in self.data:
            node = self.treeview.add_node(TreeViewLabel(text=item['Name']))
            node.add_node(TreeViewLabel(text=item['Age']))
        
    def filter_data(self, instance):
        # Filter the data based on user input
        filter_text = self.filter_input.text.lower()
        for node in self.treeview.iterate_all_nodes():
            if node.text and filter_text in node.text.lower():
                node.show()
            else:
                node.hide()

    def on_start(self):
        # Example of how to sort the table
        self.treeview._sort_func = self.sort_by_name
        self.treeview._trigger_treeview_update()

    def sort_by_name(self, items):
        # Sort the items by name
        return sorted(items, key=lambda item: item.text.lower())

    def _reverse_sort_func(self, items):
        # Reverse sort function
        return sorted(items, key=lambda item: item.text.lower(), reverse=True)

if __name__ == '__main__':
    TableSortFilterApp().run()
