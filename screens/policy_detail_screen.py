from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class PolicyDetailScreen(MDScreen):
    policy_title = StringProperty("Policy")
    policy_text = StringProperty("Policy details go here.")

    def go_back(self):
        self.manager.current = 'policy' 