from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.app import App

class FAQScreen(MDScreen):
    previous_screen = StringProperty('profile')

    def go_back(self):
        self.manager.current = self.previous_screen

    def open_cart(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'cart'

    def open_FAQ(self, FAQ_type):
        category_faqs = {
            'Delivery': [
                {'question': "Where is my order?", 'answer': "You can track your order in the 'My Orders' section."},
                {'question': "How long does delivery take?", 'answer': "Delivery usually takes 3-5 business days."},
                {'question': "Can I change my delivery address?", 'answer': "Yes, before the order is shipped."},
            ],
            'Payment': [
                {'question': "What payment methods are accepted?", 'answer': "We accept credit/debit cards, UPI, and net banking."},
                {'question': "Is my payment secure?", 'answer': "Yes, all payments are processed securely."},
                {'question': "Why was my payment declined?", 'answer': "Please check your card details or contact your bank."},
            ],
            'Account': [
                {'question': "How do I reset my password?", 'answer': "Use the 'Forgot Password' link on the login page."},
                {'question': "How do I change my email?", 'answer': "Go to account settings to update your email address."},
                {'question': "How do I delete my account?", 'answer': "Contact support to request account deletion."},
            ],
            'Product': [
                {'question': "How do I find product details?", 'answer': "Product details are listed on each product page."},
                {'question': "Are products guaranteed?", 'answer': "Yes, all products come with a standard warranty."},
                {'question': "How do I return a product?", 'answer': "Go to 'My Orders' and select the item to return."},
            ],
            'Other': [
                {'question': "How do I contact support?", 'answer': "Use the 'Contact Us' page or email support@example.com."},
                {'question': "Where can I find more info?", 'answer': "Check our Help Center for more information."},
                {'question': "How do I give feedback?", 'answer': "We welcome feedback via the app or our website."},
            ],
        }
        if FAQ_type in category_faqs:
            detail_screen = self.manager.get_screen('faq_category_detail')
            detail_screen.category_title = FAQ_type
            detail_screen.faqs = category_faqs[FAQ_type]
            self.manager.current = 'faq_category_detail'