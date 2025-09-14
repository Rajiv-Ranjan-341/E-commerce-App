from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty
from kivymd.uix.dialog import MDDialog

class PaymentScreen(MDScreen):
    upi_mode = BooleanProperty(False)
    upi_id = StringProperty("")
    upi_verified = BooleanProperty(False)

    def show_upi_card(self):
        self.upi_mode = True
        self.upi_verified = False
        self.upi_id = ""

    def verify_upi(self):
        # Simple validation: check for @ in UPI ID
        if "@" in self.upi_id and len(self.upi_id) > 5:
            self.upi_verified = True
            from kivymd.toast import toast
            toast("UPI ID verified!")
        else:
            self.upi_verified = False
            from kivymd.toast import toast
            toast("Invalid UPI ID")

    def pay_upi(self):
        if self.upi_verified:
            from kivymd.toast import toast
            toast(f"Paid via UPI: {self.upi_id}")
            self.manager.current = 'home'

    def show_how_to_find(self):
        if not hasattr(self, '_how_to_find_dialog') or self._how_to_find_dialog is None:
            self._how_to_find_dialog = MDDialog(
                title="How to find your UPI ID",
                text="Your UPI ID is usually in your payment app profile, e.g. yourname@bank",
                size_hint=(0.8, None),
                height='200dp',
            )
        self._how_to_find_dialog.open()

    def pay_by_cod(self):
        from kivymd.toast import toast
        toast('Cash on Delivery selected! (Demo)')
        self.manager.current = 'home'

    def go_back_to_order_summary(self, *args):
        self.manager.current = 'order_summary' 