from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.app import App

class OrderSummaryScreen(MDScreen):
    def on_pre_enter(self, *args):
        app = App.get_running_app()
        # Get cart and selected address
        cart = app.cart if hasattr(app, 'cart') else []
        saved_addresses_screen = self.manager.get_screen('saved_addresses')
        addresses = saved_addresses_screen.addresses
        selected_index = saved_addresses_screen.selected_index
        selected_address = addresses[selected_index] if addresses and 0 <= selected_index < len(addresses) else None
        # Update cart summary
        self.ids.summary_cart_box.clear_widgets()
        for item in cart:
            self.ids.summary_cart_box.add_widget(
                self.create_cart_item_widget(item)
            )
        # Update address summary
        if selected_address:
            self.ids.summary_address_label.text = f"[b]Shipping Address:[/b]\n{selected_address.get('name', '')}\n{selected_address.get('house', '')} {selected_address.get('road', '')}\n{selected_address.get('city', '')}, {selected_address.get('state', '')} {selected_address.get('pincode', '')}\n{selected_address.get('country', '')}\nMobile: {selected_address.get('mobile', '')}"
        else:
            self.ids.summary_address_label.text = "[b]Shipping Address:[/b]\nNot selected"
        # Update total
        total = 0
        for item in cart:
            price = item['price']
            if isinstance(price, str):
                price = price.replace('₹', '').replace(',', '').strip()
                try:
                    price = float(price)
                except ValueError:
                    price = 0
            total += price * item.get('quantity', 1)
        self.ids.summary_total_label.text = f"[b]Total:[/b] ₹ {total:.2f}"

    def create_cart_item_widget(self, item):
        from kivymd.uix.label import MDLabel
        return MDLabel(text=f"{item['name']} x{item.get('quantity', 1)} - ₹{item['price']}", font_style="Body1", size_hint_y=None, height="28dp")

    def place_order(self):
        from kivymd.toast import toast
        toast("Proceeding to payment...")
        self.manager.current = 'payment'

    def go_back_to_cart(self, *args):
        self.manager.current = 'cart' 