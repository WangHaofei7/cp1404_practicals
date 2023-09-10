from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["Bob Brown", "Cat Cyan", "Oren Ochre"]\

        def build(self):
            self.title = "Dynamic Labels"
            self.root = Builder.load_file('dynamic_labels.kv')
            self.create_labels()
            return self.root

        def create_labels(self):
            """Create labels from data and add them to the GUI."""
            for name in self.name_list:
                label = Label(text=name)
                self.root.ids.main_layout.add_widget(label)

        def clear_all_labels(self):
            """Clear all labels"""
            self.root.ids.main_layout.clear_widgets()


DynamicLabelsApp().run()