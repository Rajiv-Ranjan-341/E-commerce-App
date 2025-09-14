from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
import os

class ProductCard(MDCard):
    image = StringProperty()
    name = StringProperty()
    price = StringProperty()
    category = StringProperty()
    on_press_callback = ObjectProperty(None, allownone=True)
    is_favorite = BooleanProperty(False)

    def __init__(self, **kwargs):
        self.on_favorite_toggle = kwargs.pop('on_favorite_toggle', None)
        super().__init__(**kwargs)

    def toggle_favorite(self):
        print(f"toggle_favorite called for {self.name}, was {self.is_favorite}")  # DEBUG
        self.is_favorite = not self.is_favorite
        if self.on_favorite_toggle:
            print(f"Calling on_favorite_toggle for {self.name}, now {self.is_favorite}")  # DEBUG
            self.on_favorite_toggle(self, self.is_favorite)

    def on_image(self, instance, value):
        if not value or not os.path.exists(value):
            self.image = 'assets/default.png'  # Make sure this file exists in your assets folder 