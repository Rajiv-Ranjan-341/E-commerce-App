from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.clock import Clock
from widgets.product_card import ProductCard
from functools import partial


class HomeScreen(MDScreen):
    active_tab = StringProperty("home")

    def on_kv_post(self, base_widget):
        # Start auto-sliding the promo banner
        self.carousel_event = Clock.schedule_interval(self.auto_slide_carousel, 3)
        # self.populate_products()  # Removed to avoid ScreenManagerException

    def on_pre_enter(self, *args):
        self.populate_products()

    def populate_products(self):
        grid = self.ids.home_product_grid
        grid.clear_widgets()
        app = App.get_running_app()
        # Use the same products as in product_list_screen, but only the latest 4
        product_list_screen = app.sm.get_screen('product_list')
        latest_products = product_list_screen.products[-4:]
        for idx, product in enumerate(latest_products):
            # Map idx to the correct index in the full product list for wishlist/favorite
            real_idx = product_list_screen.products.index(product)
            # Check if product is in wishlist by name
            is_favorite = any(item['name'] == product['name'] for item in app.wishlist)
            card = ProductCard(
                image=product['image'],
                name=product['name'],
                category=product.get('category', ''),
                price=product['price'],
                is_favorite=is_favorite,
                on_favorite_toggle=product_list_screen.make_favorite_callback(real_idx)
            )
            card.on_press_callback = partial(product_list_screen.open_product_details, product)
            grid.add_widget(card)

    def auto_slide_carousel(self, dt):
        carousel = self.ids.get('promo_carousel')
        if carousel:
            if carousel.index == len(carousel.slides) - 1:
                carousel.load_slide(carousel.slides[0])
            else:
                carousel.load_next()

    def on_leave(self):
        # Stop the auto-slide when leaving the screen
        if hasattr(self, 'carousel_event'):
            self.carousel_event.cancel()

    def open_cart(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'cart'

    def open_search(self):
        if self.manager:
            self.manager.current = 'search'
    # open wishlist screen
    def open_wishlist(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'wishlist'

    def switch_tab(self, tab_name):
        self.active_tab = tab_name
        if tab_name == "home":
            self.manager.current = "home"
        elif tab_name == "list":
            self.manager.current = "category"
        elif tab_name == "profile":
            if App.get_running_app().user_logged_in:
                self.manager.current = "profile"
            else:
                self.manager.current = "account_prompt" 