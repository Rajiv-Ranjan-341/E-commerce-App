from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDIconButton
from kivy.uix.widget import Widget
from kivy.metrics import dp

class SavedCardsScreen(MDScreen):
    cards = ListProperty([])

    def on_pre_enter(self, *args):
        self.update_view()

    def update_view(self):
        container = self.ids.card_container
        add_button = self.ids.add_button
        container.clear_widgets()

        if not self.cards:
            add_button.text = "Add"
            # Add vertical space to center the empty view
            container.add_widget(Widget(size_hint_y=None, height=dp(100)))
           # container.add_widget(MDIcon(icon="wallet-outline", font_size="80sp", halign='center', theme_text_color="Custom", text_color=[0.2, 0.2, 0.2, 1]))
            container.add_widget(MDLabel(text="Oops! Your Card Holder Looks Empty.", font_style="H6", halign="center", theme_text_color="Secondary", adaptive_height=True))
            container.add_widget(MDLabel(text="Place your order with just few tap your card detail will save with us.", halign="center", theme_text_color="Hint", adaptive_height=True))
        else:
            add_button.text = "Add New Card"
            for idx, card in enumerate(self.cards):
                card_widget = self.create_card_widget(card, idx)
                container.add_widget(card_widget)
    
    def create_card_widget(self, card_data, index):
        card_box = MDCard(orientation='horizontal', padding="16dp", spacing="16dp", size_hint_y=None, height="70dp", radius=[12, 12, 12, 12], elevation=2, md_bg_color=(1,1,1,1))
        card_box.add_widget(MDIcon(icon="credit-card", pos_hint={'center_y': .5}))
        card_info = MDBoxLayout(orientation='vertical', adaptive_height=True, spacing='4dp')
        card_info.add_widget(MDLabel(text=f"**** **** **** {card_data['number'][-4:]}", font_style="Subtitle1", adaptive_height=True))
        card_info.add_widget(MDLabel(text=card_data['name'], font_style="Body2", theme_text_color="Hint", adaptive_height=True))
        card_box.add_widget(card_info)
        delete_btn = MDIconButton(icon="delete-outline", pos_hint={'center_y': .5}, on_release=lambda x, i=index: self.delete_card(i))
        card_box.add_widget(delete_btn)
        return card_box

    def add_card(self, card_data):
        self.cards.append(card_data)

    def delete_card(self, index):
        if 0 <= index < len(self.cards):
            self.cards.pop(index)
            self.update_view() 