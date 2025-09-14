from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.properties import ListProperty, NumericProperty
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from functools import partial
from kivy.clock import Clock

class SavedAddressesScreen(MDScreen):
    addresses = ListProperty([])
    selected_index = NumericProperty(-1)

    def on_pre_enter(self, *args):
        app = None
        try:
            from kivy.app import App
            app = App.get_running_app()
        except Exception:
            pass
        # Ensure prev_screen is set to last_screen if coming from add/edit address
        if app and hasattr(app, 'last_screen') and getattr(app, 'prev_screen', None) is None:
            app.prev_screen = app.last_screen
        if self.addresses and (self.selected_index < 0 or self.selected_index >= len(self.addresses)):
            self.selected_index = 0
        self.update_addresses_list()
        # Show/hide confirm button and stepper based on last_screen or prev_screen
        show_stepper = False
        if app:
            last_screen = getattr(app, 'last_screen', None)
            prev_screen = getattr(app, 'prev_screen', None)
            if last_screen == 'cart' or prev_screen == 'cart':
                show_stepper = True
        if show_stepper:
            self.ids.confirm_button.opacity = 1
            self.ids.confirm_button.disabled = False if self.addresses and 0 <= self.selected_index < len(self.addresses) else True
            self.ids.stepper_box.opacity = 1
            self.ids.stepper_box.height = 56
        else:
            self.ids.confirm_button.opacity = 0
            self.ids.confirm_button.disabled = True
            self.ids.stepper_box.opacity = 0
            self.ids.stepper_box.height = 0

    def on_selected_index(self, instance, value):
        # Update confirm button state if visible
        app = None
        try:
            from kivy.app import App
            app = App.get_running_app()
        except Exception:
            pass
        if app and hasattr(app, 'last_screen') and app.last_screen == 'cart':
            self.ids.confirm_button.disabled = False if self.addresses and 0 <= self.selected_index < len(self.addresses) else True

    def confirm_address(self):
        # Called when confirm button is pressed
        app = None
        try:
            from kivy.app import App
            app = App.get_running_app()
        except Exception:
            pass
        if self.addresses and 0 <= self.selected_index < len(self.addresses):
            # Go to order summary if coming from cart
            if app and ((hasattr(app, 'last_screen') and app.last_screen == 'cart') or (hasattr(app, 'prev_screen') and app.prev_screen == 'cart')):
                self.manager.current = 'order_summary'
                from kivymd.toast import toast
                toast('Shipping address confirmed!')
                app.last_screen = None
                app.prev_screen = None  # Clear both after use

    def update_addresses_list(self):
        addresses_box = self.ids.addresses_box
        addresses_box.clear_widgets()
        for idx, address in enumerate(self.addresses):
            card = MDCard(orientation="vertical", padding="12dp", size_hint_y=None, height="110dp", radius=[12, 12, 12, 12], md_bg_color=(1,1,1,1))
            card_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")
            card_box.add_widget(
                MDLabel(text=address.get('name', ''), font_style="Subtitle1", bold=True, size_hint_x=0.8)
            )
            card_box.add_widget(
                MDIconButton(icon="pencil-outline", on_release=lambda x, i=idx: self.edit_address(i), theme_text_color="Custom", icon_color=(0,0,0,1))
            )
            card_box.add_widget(
                MDIconButton(icon="trash-can-outline", on_release=lambda x, i=idx: self.delete_address(i), theme_text_color="Custom", icon_color=(1,0,0,1))
            )
            card.add_widget(card_box)
            card.add_widget(MDLabel(text=self.format_address(address), font_style="Body2", size_hint_y=None, height="40dp"))
            check_box_row = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp")
            checkbox = MDCheckbox(
                active=(idx == self.selected_index),
                on_active=partial(self.on_checkbox_active, idx=idx)
            )
            Clock.schedule_once(lambda dt, cb=checkbox, act=(idx == self.selected_index): setattr(cb, 'active', act), 0)
            check_box_row.add_widget(checkbox)
            check_box_row.add_widget(MDLabel(text="Use as the shipping address", font_style="Caption", size_hint_x=1))
            card.add_widget(check_box_row)
            addresses_box.add_widget(card)
        addresses_box.height = addresses_box.minimum_height

    def format_address(self, address):
        return f"{address.get('address', '')}\n{address.get('city', '')}, {address.get('state', '')} {address.get('zip', '')}, {address.get('country', '')}"

    def confirm_set_shipping_address(self, *args):
        self.selected_index = self.confirm_address_idx
        self.dialog.dismiss()
        self.update_addresses_list()

    def cancel_set_shipping_address(self, *args):
        self.dialog.dismiss()
        self.update_addresses_list()

    def delete_address(self, idx):
        if 0 <= idx < len(self.addresses):
            self.addresses.pop(idx)
            self.addresses = self.addresses  # Force update
            self.update_addresses_list()

    def edit_address(self, idx):
        if 0 <= idx < len(self.addresses):
            address = self.addresses[idx]
            add_screen = self.manager.get_screen('add_edit_address')
            name_parts = address.get('name', '').split(' ', 1)
            add_screen.ids.first_name.text = name_parts[0] if name_parts else ''
            add_screen.ids.last_name.text = name_parts[1] if len(name_parts) > 1 else ''
            add_screen.ids.mobile_number.text = address.get('mobile', '')
            add_screen.ids.pincode.text = address.get('pincode', '')
            add_screen.ids.state.text = address.get('state', '')
            add_screen.ids.city.text = address.get('city', '')
            add_screen.ids.country.text = address.get('country', '')
            add_screen.ids.house.text = address.get('house', '')
            add_screen.ids.road.text = address.get('road', '')
            add_screen.edit_index = idx
            self.manager.current = 'add_edit_address'

    def show_add_address_screen(self):
        add_screen = self.manager.get_screen('add_edit_address')
        add_screen.ids.first_name.text = ''
        add_screen.ids.last_name.text = ''
        add_screen.ids.mobile_number.text = ''
        add_screen.ids.pincode.text = ''
        add_screen.ids.state.text = ''
        add_screen.ids.city.text = ''
        add_screen.ids.country.text = ''
        add_screen.ids.house.text = ''
        add_screen.ids.road.text = ''
        add_screen.edit_index = -1
        self.manager.current = 'add_edit_address'

    def show_add_address_dialog(self):
        self.dialog = MDDialog(
            title="Add New Address",
            type="custom",
            content_cls=MDTextField(
                hint_text="Enter address",
                multiline=True,
            ),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=self.close_dialog),
                MDFlatButton(text="ADD", on_release=self.add_address),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def add_address(self, *args):
        address = self.dialog.content_cls.text.strip()
        if address:
            self.addresses.append(address)
            self.update_addresses_list()
        self.dialog.dismiss()

    def go_back(self):
        self.manager.current = 'profile'

    def on_checkbox_active(self, checkbox, value, idx):
        print(f"[DEBUG] on_checkbox_active called: idx={idx}, value={value}, selected_index={self.selected_index}")
        if value and idx != self.selected_index:
            self.confirm_address_idx = idx
            self.dialog = MDDialog(
                title="Confirm Address",
                text="Use this address for shipping?",
                buttons=[
                    MDFlatButton(text="CANCEL", on_release=self.cancel_set_shipping_address),
                    MDFlatButton(text="CONFIRM", on_release=self.confirm_set_shipping_address),
                ],
            )
            self.dialog.open()
        elif not value and idx == self.selected_index:
            print(f"[DEBUG] Preventing uncheck of selected address idx={idx}")
            checkbox.active = True  # Prevent unchecking the selected address 

    def on_leave(self, *args):
        # Only clear last_screen and prev_screen if not navigating to add_edit_address
        try:
            from kivy.app import App
            app = App.get_running_app()
            next_screen = self.manager.current if hasattr(self.manager, 'current') else None
            if next_screen != 'add_edit_address':
                if hasattr(app, 'last_screen'):
                    app.last_screen = None
                if hasattr(app, 'prev_screen'):
                    app.prev_screen = None
        except Exception:
            pass 