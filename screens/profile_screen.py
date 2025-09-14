from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivy.app import App

class ClickableRow(ButtonBehavior, MDBoxLayout):
    pass

class ProfileScreen(MDScreen):
    avatar_source = StringProperty('assets/my_avatar.png')
    current_name = StringProperty('who_AM')
    current_email = StringProperty('whN@example.com')
    active_tab = StringProperty("profile")

    def on_enter(self, *args):
        if not App.get_running_app().user_logged_in:
            self.manager.current = 'home'
            return
        print(f"[DEBUG] Profile avatar source: {self.avatar_source}")

    def go_to_orders(self):
        self.manager.current = 'orders'

    def go_to_addresses(self):
        self.manager.current = 'saved_addresses'

    def go_to_edit_profile(self):
        edit_screen = self.manager.get_screen('edit_profile')
        edit_screen.current_name = self.current_name
        edit_screen.current_email = self.current_email
        self.manager.current = 'edit_profile'

    def log_out(self):
        App.get_running_app().user_logged_in = False
        self.manager.current = 'login'

    def go_to_notification_settings(self):
        self.manager.current = 'notification'

    def go_to_cards(self):
        self.manager.current = 'saved_cards'

    def go_to_privacy_center(self):
        self.manager.current = 'privacy'

    def go_to_help_center(self):
        self.manager.current = 'help_center'

    def go_to_wishlist(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'wishlist'

    def go_to_terms(self):
        policy_screen = self.manager.get_screen('policy')
        policy_screen.previous_screen = 'profile'
        self.manager.current = 'policy'

    def go_to_faq(self):
        faq_screen = self.manager.get_screen('FAQ')
        faq_screen.previous_screen = 'profile'
        self.manager.current = 'FAQ'

    def go_to_cart(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'cart'

    def switch_tab(self, tab_name):
        self.active_tab = tab_name
        if tab_name == "home":
            self.manager.current = "home"
        elif tab_name == "list":
            self.manager.current = "orders"
        elif tab_name == "profile":
            self.manager.current = "profile"

class AccountPromptScreen(MDScreen):
    active_tab = StringProperty("profile")

    def go_to_login(self):
        app = App.get_running_app()
        app.last_screen = 'account_prompt'
        self.manager.current = 'login'

    def go_to_notification_settings(self):
        self.manager.current = 'notification'

    def go_to_help_center(self):
        self.manager.current = 'help_center'

    def go_to_terms(self):
        policy_screen = self.manager.get_screen('policy')
        policy_screen.previous_screen = 'account_prompt'
        self.manager.current = 'policy'

    def go_to_faqs(self):
        faq_screen = self.manager.get_screen('FAQ')
        faq_screen.previous_screen = 'account_prompt'
        self.manager.current = 'FAQ'

    def switch_tab(self, tab_name):
        self.active_tab = tab_name
        if tab_name == "home":
            self.manager.current = "home"
        elif tab_name == "list":
            self.manager.current = "orders"
        elif tab_name == "profile":
            self.manager.current = "account_prompt"