from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class PrivacyScreen(MDScreen):
    dialog = None

    def delete_account(self):
        # Show a confirmation dialog
        self.dialog = MDDialog(
            title="Delete Account",
            text="Are you sure you want to delete your account? This action cannot be undone.",
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                MDFlatButton(text="DELETE", text_color=(1,0.2,0.2,1), on_release=self.confirm_delete)
            ],
        )
        self.dialog.open()

    def confirm_delete(self, *args):
        self.dialog.dismiss()
        # Here you would add real deletion logic (API call, etc.)
        # For now, just log out and show a message
        self.manager.current = 'login'
        self.dialog = MDDialog(
            title="Account Deleted",
            text="Your account has been deleted.",
            buttons=[
                MDFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())
            ],
        )
        self.dialog.open() 