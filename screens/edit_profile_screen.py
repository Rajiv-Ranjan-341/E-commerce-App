from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.uix.pickers import MDDatePicker
import datetime

class EditProfileScreen(MDScreen):
    current_name = StringProperty('John Doe')
    current_email = StringProperty('john.doe@example.com')
    current_phone = StringProperty('+1234567890')
    current_dob = StringProperty('01/01/1990')

    def on_enter(self, *args):
        # Populate fields when the screen is entered
        if self.current_name and ' ' in self.current_name:
            first_name, last_name = self.current_name.split(' ', 1)
        else:
            first_name, last_name = self.current_name, ''
        
        self.ids.first_name_field.text = first_name
        self.ids.last_name_field.text = last_name
        self.ids.email_field.text = self.current_email
        self.ids.phone_field.text = self.current_phone
        self.ids.dob_field.text = self.current_dob

    def show_date_picker(self):
        # Set initial date
        try:
            initial_date = datetime.datetime.strptime(self.ids.dob_field.text, '%d/%m/%Y').date()
        except (ValueError, TypeError):
            initial_date = datetime.date.today()

        date_dialog = MDDatePicker(
            year=initial_date.year,
            month=initial_date.month,
            day=initial_date.day,
        )
        date_dialog.bind(on_save=self.on_date_save)
        date_dialog.open()

    def on_date_save(self, instance, value, date_range):
        if value:
            self.ids.dob_field.text = value.strftime('%d/%m/%Y')
            self.current_dob = self.ids.dob_field.text
            self.ids.dob_field.focus = False

    def save_profile_changes(self):
        self.current_name = f"{self.ids.first_name_field.text} {self.ids.last_name_field.text}".strip()
        self.current_email = self.ids.email_field.text
        self.current_phone = self.ids.phone_field.text
        self.current_dob = self.ids.dob_field.text
        
        profile_screen = self.manager.get_screen('profile')
        profile_screen.current_name = self.current_name
        profile_screen.current_email = self.current_email

        self.manager.current = 'profile'
        print("Profile Saved:", self.current_name, self.current_email, self.current_phone, self.current_dob)