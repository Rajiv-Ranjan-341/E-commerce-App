from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.clock import Clock

class DoubleTapCarousel(Carousel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._last_touch_time = 0
        self._double_tap_time = 0.3  # seconds

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            now = Clock.get_time()
            if now - self._last_touch_time < self._double_tap_time:
                # Double tap detected
                x = touch.x
                if x > self.center_x:
                    self.load_next()
                else:
                    self.load_previous()
                self._last_touch_time = 0  # reset
                return True
            self._last_touch_time = now
        return super().on_touch_down(touch)

class ProductDetailsScreen(MDScreen):
    product_name = StringProperty("")
    product_price = NumericProperty(0)
    product_images = ListProperty([])
    product_description = StringProperty("")
    product_category = StringProperty("")
    is_in_wishlist = BooleanProperty(False)

    def set_product(self, name, price, images, description, category):
        print("Product images:", images)  # DEBUG
        self.product_name = name
        self.product_price = price
        self.product_images = images
        self.product_description = description
        self.product_category = category
        # Check if product is in wishlist
        app = App.get_running_app()
        self.is_in_wishlist = any(item['name'] == name for item in app.wishlist)

    def on_product_images(self, instance, value):
        if not self.ids.get('image_carousel'):
            return
        carousel = self.ids.image_carousel
        carousel.clear_widgets()
        from kivymd.uix.fitimage import FitImage
        for img in value:
            carousel.add_widget(FitImage(source=img, radius=[12,], size_hint=(1, 1)))

    def go_back(self):
        # Reset carousel to first image
        if self.ids.get('image_carousel'):
            self.ids.image_carousel.index = 0
        app = App.get_running_app()
        if app and hasattr(app, 'last_screen'):
            app.sm.current = app.last_screen
        else:
            app.sm.current = 'product_list'

    def toggle_wishlist(self):
        """Toggle wishlist status for the current product"""
        app = App.get_running_app()
        self.is_in_wishlist = not self.is_in_wishlist
        
        # Update the wishlist in the app
        if self.is_in_wishlist:
            # Add to wishlist
            wishlist_item = {
                'name': self.product_name,
                'image': self.product_images[0] if self.product_images else '',
                'price': self.product_price,
                'category': self.product_category
            }
            # Check if already in wishlist
            if not any(item['name'] == self.product_name for item in app.wishlist):
                app.wishlist.append(wishlist_item)
                print(f"Product {self.product_name} added to wishlist")
        else:
            # Remove from wishlist
            app.wishlist = [item for item in app.wishlist if item['name'] != self.product_name]
            print(f"Product {self.product_name} removed from wishlist")

    def share_product(self):
        """Share product details (placeholder for future implementation)"""
        print(f"Sharing product: {self.product_name}")
        # Here you can implement actual sharing functionality
        # For now, just print to console

    def add_to_cart(self):
        app = App.get_running_app()
        cart_item = {
            'name': self.product_name,
            'price': self.product_price,
            'image': self.product_images[0] if self.product_images else '',
            'category': self.product_category,
            'quantity': 1
        }
        for item in app.cart:
            if item['name'] == cart_item['name']:
                item['quantity'] += 1
                break
        else:
            app.cart.append(cart_item)
        print(f"Added {self.product_name} to cart. Cart now: {app.cart}")
        app.sm.current = 'cart'

    def buy_now(self):
        """Buy now functionality"""
        app = App.get_running_app()
        print(f"Buying {self.product_name} now")
        # Here you can implement actual purchase functionality
        # For now, just print to console and navigate to cart
        app.sm.current = 'cart' 