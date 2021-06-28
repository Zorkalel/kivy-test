from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.image import Image as CoreImage
from kivy.uix.boxlayout import BoxLayout


# Configuration of screen
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '480')

# Main widget of the program
class MainWidget(Widget):
    pass

class BoxLayoutTest(BoxLayout):
    """ #comment
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.add_widget(CoreImage(source='flag.png'))
        self.add_widget(CoreImage(source='flag.png'))
        """    
    pass


# just function to testex
class TestApp(App):
    # def build(self):
        # Im = CoreImage(source="flag.png")
        # Im.pos=(50,50)
        # return Im
    pass

TestApp().run()