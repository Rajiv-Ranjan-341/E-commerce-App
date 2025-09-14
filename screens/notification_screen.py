from kivymd.uix.screen import MDScreen

class NotificationScreen(MDScreen):
    def go_back(self):
        self.manager.current = 'profile'  # or your desired screen

    def go_to_home(self):
        self.manager.current = 'profile'  # or your home screen 