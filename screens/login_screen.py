from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import re
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.app import App

class LoginScreen(MDScreen):
    def show_error(self, message):
        dialog = MDDialog(
            title="Invalid Input",
            text=message,
            buttons=[
                MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
            ],
        )
        dialog.open()

    def login(self):
        email = self.ids.login_email.text.strip()
        password = self.ids.login_password.text.strip()
        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_error("Please enter a valid email address.")
            return
        # Password validation
        if len(password) < 6:
            self.show_error("Password must be at least 6 characters long.")
            return
        print(f"Login with {email} / {password}")
        App.get_running_app().user_logged_in = True
        self.manager.current = 'profile'

    def switch_to_register(self):
        self.manager.current = 'register'

    def go_to_account_prompt(self):
        app = App.get_running_app()
        if hasattr(app, 'last_screen') and app.last_screen and app.last_screen != 'login':
            self.manager.current = app.last_screen
        else:
            self.manager.current = 'account_prompt'

class RegisterScreen(MDScreen):
    def show_error(self, message):
        dialog = MDDialog(
            title="Invalid Input",
            text=message,
            buttons=[
                MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
            ],
        )
        dialog.open()

    def register(self):
        name = self.ids.register_name.text.strip()
        email = self.ids.register_email.text.strip()
        password = self.ids.register_password.text.strip()
        confirm_password = self.ids.register_confirm_password.text.strip()
        # Name validation
        if not name:
            self.show_error("Please enter your full name.")
            return
        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_error("Please enter a valid email address.")
            return
        # Password validation
        if len(password) < 6:
            self.show_error("Password must be at least 6 characters long.")
            return
        if password != confirm_password:
            self.show_error("Passwords do not match.")
            return
        print(f"Register with {email} / {password}")
        App.get_running_app().user_logged_in = True
        self.manager.current = 'profile'

    def switch_to_login(self):
        self.manager.current = 'login' 