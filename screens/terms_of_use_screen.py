from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class TermsOfUseScreen(MDScreen):
    terms_text = StringProperty(
        "Your Terms Of Use go here. You can write as much as you want. "
        "This is just a placeholder for demonstration."
    )

    def go_back(self):
        self.manager.current = 'policy' 