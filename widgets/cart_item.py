from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, BooleanProperty
from kivy.app import App

class CartItem(MDBoxLayout):
    product_name = StringProperty("")
    product_image = StringProperty("")
    product_price = NumericProperty(0)
    product_quantity = NumericProperty(1)
    on_remove = ObjectProperty(None)
    is_in_wishlist = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("CartItem __init__:", self.product_name, "on_remove:", self.on_remove)
        # Check if item is in wishlist
        self.update_wishlist_status()

    def update_wishlist_status(self):
        """Update the wishlist status of this item"""
        app = App.get_running_app()
        self.is_in_wishlist = any(item['name'] == self.product_name for item in app.wishlist)

    def on_move_to_wishlist(self, instance):
        """Toggle item in wishlist (add if not there, remove if there)"""
        app = App.get_running_app()
        
        if self.is_in_wishlist:
            # Remove from wishlist
            print(f"Removing {self.product_name} from wishlist")  # Debug print
            app.wishlist = [item for item in app.wishlist if item['name'] != self.product_name]
            self.is_in_wishlist = False
            print(f"Removed from wishlist. Wishlist now has {len(app.wishlist)} items")  # Debug print
        else:
            # Add to wishlist
            print(f"Adding {self.product_name} to wishlist")  # Debug print
            wishlist_item = {
                'name': self.product_name,
                'image': self.product_image,
                'price': self.product_price
            }
            app.wishlist.append(wishlist_item)
            self.is_in_wishlist = True
            print(f"Added to wishlist. Wishlist now has {len(app.wishlist)} items")  # Debug print
        
        # Don't remove from cart - keep item in cart regardless of wishlist status

from kivy.lang import Builder
Builder.load_file("widgets/cart_item.kv") 