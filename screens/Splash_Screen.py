from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.clock import Clock

class SplashScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.start_animation, 0.1)

    def start_animation(self, *args):
        logo = self.ids.logo
        Animation(opacity=1, size_hint=(0.7, 0.7), duration=3).start(logo)
        Clock.schedule_once(self.switch_to_home, 3.5)

    def switch_to_home(self, *args):
        self.manager.current = "home"
