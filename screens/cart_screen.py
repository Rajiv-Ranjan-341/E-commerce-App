from kivymd.uix.screen import MDScreen
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App
from functools import partial
from kivymd.toast import toast

class CartScreen(MDScreen):
    cart_count = NumericProperty(0)

    def get_cart_total(self):
        app = App.get_running_app()
        total = 0
        for item in app.cart:
            price = item['price']
            if isinstance(price, str):
                price = price.replace('₹', '').replace(',', '').strip()
                try:
                    price = float(price)
                except ValueError:
                    price = 0
            total += price * item.get('quantity', 1)
        return total

    def get_cart_count(self):
        app = App.get_running_app()
        return sum(item.get('quantity', 1) for item in app.cart)

    def get_grand_total(self):
        subtotal = self.get_cart_total()
        gst = round(subtotal * 0.12, 2) if subtotal > 0 else 0
        shipping = 0 if subtotal >= 1000 else 50 if subtotal > 0 else 0
        grand_total = subtotal + gst + shipping
        return grand_total

    def update_bill(self):
        subtotal = self.get_cart_total()
        gst = round(subtotal * 0.12, 2) if subtotal > 0 else 0
        shipping = 0 if subtotal >= 1000 else 50 if subtotal > 0 else 0
        shipping_str = "[color=00897B]Free[/color] [s]₹ 50.00[/s]" if shipping == 0 and subtotal > 0 else f"₹ {shipping:.2f}"
        grand_total = subtotal + gst + shipping

        self.ids.subtotal_label.text = f"₹ {subtotal:.2f}"
        self.ids.gst_label.text = f"₹ {gst:.2f}"
        self.ids.shipping_label.text = shipping_str
        self.ids.grand_total_label.text = f"₹ {grand_total:,.0f}"

    def on_pre_enter(self, *args):
        print("CartScreen on_pre_enter called")  # DEBUG
        app = App.get_running_app()
        self.cart_count = self.get_cart_count()

        cart_box = self.ids.get('cart_items_box')
        bill_box = self.ids.get('bill_box')
        bottom_bar = self.ids.get('bottom_bar')
        total_label = self.ids.get('total_label')
        print("cart_box:", cart_box)  # DEBUG
        print("app.cart in cart screen:", app.cart)  # DEBUG
        
        if cart_box:
            cart_box.clear_widgets()
            if app.cart:
                # Only add CartItem widgets to cart_items_box
                from widgets.cart_item import CartItem
                for item in app.cart:
                    ci = CartItem(
                        product_name=item['name'],
                        product_image=item['image'],
                        product_price=item['price'],
                        product_quantity=item['quantity'],
                    )
                    ci.on_remove = self.remove_cart_item
                    ci.update_wishlist_status()
                    cart_box.add_widget(ci)
                # Show bill
                if bill_box:
                    bill_box.opacity = 1
                    bill_box.disabled = False
            else:
                # Add empty cart labels to cart_items_box if needed
                from kivymd.uix.label import MDLabel
                empty_cart_label = MDLabel(
                    text="Your shopping cart is empty.",
                    halign='center',
                    theme_text_color='Primary',
                    font_style='Subtitle1',
                    bold=True,
                    size_hint_y=None,
                    height='40dp'
                )
                empty_cart_hint = MDLabel(
                    text="Please add something soon, carts have feelings too.",
                    halign='center',
                    theme_text_color='Hint',
                    font_style='Body2',
                    size_hint_y=None,
                    height='30dp'
                )
                cart_box.add_widget(empty_cart_label)
                cart_box.add_widget(empty_cart_hint)
                # Hide bill
                if bill_box:
                    bill_box.opacity = 0
                    bill_box.disabled = True

        # Show/hide bottom bar as before
        if app.cart:
            if bottom_bar:
                bottom_bar.opacity = 1
                bottom_bar.disabled = False
        else:
            if bottom_bar:
                bottom_bar.opacity = 0
                bottom_bar.disabled = True

        # Update total label and bill
        if total_label:
            total_label.text = f"₹ {self.get_grand_total():.2f}" if app.cart else "₹ 0.00"
        self.update_bill()

    def remove_cart_item(self, cart_item_widget):
        print("remove_cart_item called for:", cart_item_widget.product_name)
        app = App.get_running_app()
        # Remove from app.cart by name
        app.cart = [item for item in app.cart if item['name'] != cart_item_widget.product_name]
        self.on_pre_enter()

    def go_back(self):
        app = App.get_running_app()
        if app.last_screen and app.last_screen != 'cart':
            self.manager.current = app.last_screen
        else:
            self.manager.current = 'home'
    
    def open_wishlist(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'wishlist'

    def go_to_login(self):
        app = App.get_running_app()
        app.last_screen = 'cart'
        app.root.current = 'login'

    def handle_continue(self):
        app = App.get_running_app()
        if app.user_logged_in:
            # Get the saved addresses screen
            saved_addresses_screen = self.manager.get_screen('saved_addresses')
            addresses = saved_addresses_screen.addresses
            selected_index = saved_addresses_screen.selected_index
            # Check if there is at least one address and a selected address
            if not addresses or selected_index < 0 or selected_index >= len(addresses):
                # Set last_screen to 'cart' so confirm button appears
                app.last_screen = 'cart'
                # Redirect to saved addresses screen
                self.manager.current = 'saved_addresses'
                toast("Please select or add a shipping address")
            else:
                # Go to order summary screen
                self.manager.current = 'order_summary'
        else:
            print("User not logged in, redirecting to login")  # DEBUG
            app.last_screen = 'cart'
            self.manager.current = 'login'