from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from widgets.product_card import ProductCard
from kivy.factory import Factory
from kivy.app import App

class WishlistScreen(MDScreen):
    previous_screen = None

    def go_back(self):
        app = App.get_running_app()
        if hasattr(app, 'last_screen') and app.last_screen:
            self.manager.current = app.last_screen
        else:
            self.manager.current = 'home'

    def set_wishlist(self, products):
        grid = self.ids.wishlist_grid
        grid.clear_widgets()
        if not products:
            from kivymd.uix.label import MDLabel
            grid.add_widget(MDLabel(text='No items in wishlist', halign='center', font_style='H6', size_hint_y=None, height='40dp'))
            return
        for product in products:
            # Convert price to string if it's numeric
            price_str = str(product['price']) if isinstance(product['price'], (int, float)) else product['price']
            card = ProductCard(
                image=product['image'],
                name=product['name'],
                price=price_str,
                category=product.get('category', ''),
                is_favorite=True,
                on_favorite_toggle=lambda card, fav, name=product['name']: self.remove_from_wishlist(name) if not fav else None
            )
            grid.add_widget(card)
        # Center single product in grid
        if len(products) == 1:
            grid.add_widget(Widget())

    def remove_from_wishlist(self, product_name):
        app = App.get_running_app()
        # Remove from wishlist by name
        app.wishlist = [item for item in app.wishlist if item['name'] != product_name]
        # Refresh the wishlist display
        self.set_wishlist(app.wishlist)

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        # Track the previous screen
        if self.manager:
            self.previous_screen = self.manager.current_screen.name if self.manager.current_screen.name != 'wishlist' else self.previous_screen
        # Display wishlist items directly from app.wishlist
        self.set_wishlist(app.wishlist)

    def open_cart(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'cart' 