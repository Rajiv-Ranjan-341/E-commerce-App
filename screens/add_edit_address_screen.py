from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty

class AddEditAddressScreen(MDScreen):
    edit_index = NumericProperty(-1)
    def save_address(self):
        print("IDS:", self.ids.keys())
        first_name = self.ids.first_name.text.strip()
        last_name = self.ids.last_name.text.strip()
        mobile_number = self.ids.mobile_number.text.strip()
        pincode = self.ids.pincode.text.strip()
        state = self.ids.state.text.strip()
        city = self.ids.city.text.strip()
        country = self.ids.country.text.strip()
        house = self.ids.house.text.strip()
        road = self.ids.road.text.strip()
        if first_name and last_name and mobile_number and pincode and state and city and country and house and road:
            address_obj = {
                'name': f"{first_name} {last_name}",
                'mobile': mobile_number,
                'pincode': pincode,
                'state': state,
                'city': city,
                'country': country,
                'house': house,
                'road': road
            }
            saved_addresses_screen = self.manager.get_screen('saved_addresses')
            if self.edit_index != -1:
                saved_addresses_screen.addresses[self.edit_index] = address_obj
                self.edit_index = -1
            else:
                saved_addresses_screen.addresses.append(address_obj)
            saved_addresses_screen.addresses = saved_addresses_screen.addresses  # Force update
            saved_addresses_screen.update_addresses_list()
        # Track navigation history for stepper/confirm logic
        try:
            from kivy.app import App
            app = App.get_running_app()
            if hasattr(app, 'prev_screen') and app.prev_screen == 'cart':
                app.last_screen = 'cart'
        except Exception:
            pass
        self.manager.current = 'saved_addresses' 