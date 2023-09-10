from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """The StringProperty is for the text on the output (km) label."""
    output_label = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        """default value for output label"""
        self.output_label = '0.0'
        return self.root

    def handle_increment(self, step):
        """handle up/down button press"""
        new_miles = self.get_input_miles() + step
        self.root.ids.input_miles.text = str(new_miles)

    def get_input_miles(self):
        try:
           miles = float(self.root.ids.input_miles.text)
           return miles
        except ValueError:
           return 0.0

    def handle_calculate(self):
        result = self.get_input_miles() * MILES_TO_KM
        self.output_label = str(result)


MilesConverterApp().run()