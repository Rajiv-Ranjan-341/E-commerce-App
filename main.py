from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from screens.Splash_Screen import SplashScreen
from screens.profile_screen import ProfileScreen, AccountPromptScreen
from screens.orders_screen import OrdersScreen
from screens.login_screen import LoginScreen, RegisterScreen
from screens.edit_profile_screen import EditProfileScreen
from screens.saved_addresses_screen import SavedAddressesScreen
from screens.add_edit_address_screen import AddEditAddressScreen
from screens.notification_screen import NotificationScreen
from screens.saved_cards_screen import SavedCardsScreen
from screens.add_card_screen import AddCardScreen
from screens.privacy_screen import PrivacyScreen
from screens.help_center_screen import HelpCenterScreen
from screens.policy_screen import PolicyScreen
from screens.terms_of_use_screen import TermsOfUseScreen
from screens.policy_detail_screen import PolicyDetailScreen
from screens.FAQ_screen import FAQScreen
from screens.faq_category_detail_screen import FAQCategoryDetailScreen
from screens.home_screen import HomeScreen
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from screens.search_screen import SearchScreen
from screens.product_list_screen import ProductListScreen
from screens.wishlist_screen import WishlistScreen
from screens.category_screen import CategoryScreen
from screens.cart_screen import CartScreen
from screens.product_details_screen import ProductDetailsScreen
from screens.order_summary_screen import OrderSummaryScreen
from screens.payment_screen import PaymentScreen

# Set window size for mobile-like experience
Window.size = (400, 700)

class EcommerceApp(MDApp):
    user_logged_in = False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.wishlist = []  # Initialize as empty list to store wishlist items
        self.last_screen = None
        self.cart = []  # List to store cart items
        
    def build(self):
        # Load all KV files from the correct directory
        Builder.load_file('screens/Splash_Screen.kv')
        Builder.load_file('screens/profile_screen.kv')
        Builder.load_file('screens/orders_screen.kv')
        Builder.load_file('screens/login_screen.kv')
        Builder.load_file('screens/edit_profile_screen.kv')
        Builder.load_file('screens/saved_addresses_screen.kv')
        Builder.load_file('screens/add_edit_address_screen.kv')
        Builder.load_file('screens/notification_screen.kv')
        Builder.load_file('screens/saved_cards_screen.kv')
        Builder.load_file('screens/add_card_screen.kv')
        Builder.load_file('screens/privacy_screen.kv')
        Builder.load_file('screens/help_center_screen.kv')
        Builder.load_file('screens/policy_screen.kv')
        Builder.load_file('screens/terms_of_use_screen.kv')
        Builder.load_file('screens/policy_detail_screen.kv')
        Builder.load_file('screens/FAQ_screen.kv')
        Builder.load_file('screens/faq_category_detail_screen.kv')
        Builder.load_file('screens/home_screen.kv')
        Builder.load_file('screens/search_screen.kv')
        Builder.load_file('screens/product_list_screen.kv')
        Builder.load_file('screens/wishlist_screen.kv')
        Builder.load_file('screens/category_screen.kv')
        Builder.load_file('screens/cart_screen.kv')
        Builder.load_file('screens/product_details_screen.kv')
        Builder.load_file('screens/order_summary_screen.kv')
        Builder.load_file('screens/payment_screen.kv')

        # Create screen manager and add all screens
        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen(name='splash'))
        self.sm.add_widget(AccountPromptScreen(name='account_prompt'))
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(ProfileScreen(name='profile'))
        self.sm.add_widget(OrdersScreen(name='orders'))
        self.sm.add_widget(EditProfileScreen(name='edit_profile'))
        self.sm.add_widget(SavedAddressesScreen(name='saved_addresses'))
        self.sm.add_widget(AddEditAddressScreen(name='add_edit_address'))
        self.sm.add_widget(NotificationScreen(name='notification'))
        self.sm.add_widget(SavedCardsScreen(name='saved_cards'))
        self.sm.add_widget(AddCardScreen(name='add_card'))
        self.sm.add_widget(PrivacyScreen(name='privacy'))
        self.sm.add_widget(HelpCenterScreen(name='help_center'))
        self.sm.add_widget(PolicyScreen(name='policy'))
        self.sm.add_widget(TermsOfUseScreen(name='terms_of_use'))
        self.sm.add_widget(PolicyDetailScreen(name='policy_detail'))
        self.sm.add_widget(FAQScreen(name='FAQ'))
        self.sm.add_widget(FAQCategoryDetailScreen(name='faq_category_detail'))
        self.sm.add_widget(HomeScreen(name='home'))  # <-- This is critical!
        self.sm.add_widget(SearchScreen(name='search'))
        self.sm.add_widget(ProductListScreen(name='product_list'))
        self.sm.add_widget(WishlistScreen(name='wishlist'))
        self.sm.add_widget(CategoryScreen(name='category'))
        self.sm.add_widget(CartScreen(name='cart'))
        self.sm.add_widget(ProductDetailsScreen(name='product_details'))
        self.sm.add_widget(OrderSummaryScreen(name='order_summary'))
        self.sm.add_widget(PaymentScreen(name='payment'))

        self.sm.current = 'splash'  # Set after all screens are added
        return self.sm

    def go_to_orders(self):
        self.sm.current = 'orders'

class OrdersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Example static data; replace with your real data source
        self.all_orders = [
            {"product_name": "Peperomia Flex"},
            {"product_name": "Aloe Vera"},
            {"product_name": "Snake Plant"},
            {"product_name": "Peperomia Flex"},
        ]

    def on_pre_enter(self, *args):
        self.filter_orders(self.ids.order_search_field.text)

    def filter_orders(self, search_text):
        container = self.ids['order_list_container']
        container.clear_widgets()
        search_text = search_text.lower()
        for order in self.all_orders:
            if search_text in order["product_name"].lower():
                container.add_widget(
                    self.create_order_item(order["product_name"])
                )

    def create_order_item(self, product_name):
        from kivy.lang import Builder
        return Builder.load_string(f'''
OrderItem:
    product_name: "{product_name}"
''')

    def go_back(self):
        self.manager.current = 'profile'

    # def open_cart(self):
    #     app = App.get_running_app()
    #     app.last_screen = self.manager.current_screen.name
    #     self.manager.current = 'cart'

if __name__ == '__main__':
    EcommerceApp().run() 