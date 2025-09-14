from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class FAQItem(BoxLayout):
    def __init__(self, question, answer, **kwargs):
        super().__init__(orientation='vertical', spacing=0, padding=[0, 0, 0, 0], size_hint_y=None, **kwargs)
        # Question label
        self.question_lbl = Label(
            text=question,
            size_hint_y=None,
            height=0,
            color=(0, 0, 0, 1),
            bold=True,
            font_size='16sp',
            halign='left',
            valign='middle',
        )
        # Answer label
        self.answer_lbl = Label(
            text=answer,
            size_hint_y=None,
            height=0,
            color=(0.2, 0.2, 0.2, 1),
            font_size='14sp',
            halign='left',
            valign='top',
        )
        self.question_lbl.bind(width=self._update_text_size)
        self.answer_lbl.bind(width=self._update_text_size)
        self.add_widget(self.question_lbl)
        self.add_widget(self.answer_lbl)
        # Divider
        self.divider = Widget(size_hint_y=None, height=1)
        self.add_widget(self.divider)
        with self.divider.canvas:
            Color(0.9, 0.9, 0.9, 1)
            self.divider_line = Rectangle(size=(0, 1), pos=(0, 0))
        self.divider.bind(size=self._update_divider, pos=self._update_divider)
        # Update height after layout
        self.bind(children=self._update_height)
        self._update_height()

    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)
        instance.texture_update()
        instance.height = instance.texture_size[1] + 12
        self._update_height()

    def _update_height(self, *args):
        total_height = sum(child.height for child in self.children)
        self.height = total_height

    def _update_divider(self, *args):
        self.divider_line.size = (self.divider.width, 1)
        self.divider_line.pos = (self.divider.x, self.divider.y)

class HelpCenterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faq_items = [
            {
                'question': 'How do I reset my password?',
                'answer': 'Go to the login screen, tap "Forgot password?", and follow the instructions sent to your email.'
            },
            {
                'question': 'How can I contact support?',
                'answer': 'You can contact support via the Help Center or by emailing support@yourapp.com.'
            },
        ]

    def on_enter(self):
        self.update_faq_list()

    def update_faq_list(self):
        faq_accordion = self.ids.faq_accordion
        faq_accordion.clear_widgets()
        for item in self.faq_items:
            faq_item = FAQItem(item['question'], item['answer'])
            faq_accordion.add_widget(faq_item) 