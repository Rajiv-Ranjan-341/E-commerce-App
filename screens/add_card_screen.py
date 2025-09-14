from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
import datetime

class AddCardScreen(MDScreen):
    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_year=datetime.date.today().year,
            max_year=datetime.date.today().year + 10,
        )
        date_dialog.bind(on_save=self.on_date_save)
        date_dialog.open()

    def on_date_save(self, instance, value, date_range):
        if value:
            self.ids.expiry_date_field.text = value.strftime('%m/%y')

    def add_card(self):
        card_number = self.ids.card_number_field.text
        expiry_date = self.ids.expiry_date_field.text
        card_holder_name = self.ids.card_holder_name_field.text

        if not (card_number and expiry_date and card_holder_name):
            print("Form is not complete")
            return

        new_card_data = {
            'number': card_number,
            'expiry': expiry_date,
            'name': card_holder_name
        }

        saved_cards_screen = self.manager.get_screen('saved_cards')
        saved_cards_screen.add_card(new_card_data)

        self.manager.current = 'saved_cards' 