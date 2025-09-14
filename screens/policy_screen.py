from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class PolicyScreen(MDScreen):
    previous_screen = StringProperty('profile')

    def go_back(self):
        self.manager.current = self.previous_screen

    def open_policy(self, policy_type):
        policy_map = {
            'terms': ("Terms of Use", "Your Terms of Use go here..."),
            'privacy': ("Privacy Policy", "Your Privacy Policy goes here..."),
            'affiliate': ("Affiliate Policy", "Your Affiliate Policy goes here..."),
            'infringement': ("Infringement Policy", "Your Infringement Policy goes here..."),
            'license': ("License", "Your License details go here..."),
            'return': ("Return Policy", "Your Return Policy goes here..."),
        }
        if policy_type == 'terms':
            self.manager.current = 'terms_of_use'
        elif policy_type == 'privacy':
            self.manager.current = 'policy_detail' 
        elif policy_type in policy_map:
            title, text = policy_map[policy_type]
            detail_screen = self.manager.get_screen('policy_detail')
            detail_screen.policy_title = title
            detail_screen.policy_text = text
            self.manager.current = 'policy_detail'
        else:
            print(f"Open policy: {policy_type}")

