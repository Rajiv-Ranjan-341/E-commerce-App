from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivymd.uix.toolbar import MDTopAppBar
from kivy.app import App

class OrdersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        # Sample order data
        self.orders = {
            "Delivered": [
                {
                    "id": "12345",
                    "date": "2024-03-15",
                    "status": "Delivered",
                    "item": "Nike Air Max",
                    "color": (0, 0.7, 0, 1)  # Green
                },
                {
                    "id": "12346",
                    "date": "2024-03-10",
                    "status": "Delivered",
                    "item": "Adidas Ultraboost",
                    "color": (0, 0.7, 0, 1)
                }
            ],
            "Processing": [
                {
                    "id": "12347",
                    "date": "2024-03-20",
                    "status": "Processing",
                    "item": "Puma RS-X",
                    "color": (1, 0.6, 0, 1)  # Orange
                }
            ],
            "Cancelled": [
                {
                    "id": "12348",
                    "date": "2024-03-05",
                    "status": "Cancelled",
                    "item": "New Balance 574",
                    "color": (1, 0, 0, 1)  # Red
                }
            ]
        }
        
        # Show initial tab (Delivered)
        self.switch_tab(0)
    
    def switch_tab(self, tab_index):
        # Clear existing orders
        self.ids.order_list.clear_widgets()
        
        # Get orders for selected tab
        tab_name = ["Delivered", "Processing", "Cancelled"][tab_index]
        orders = self.orders[tab_name]
        
        # Add order cards
        for order in orders:
            card = OrderCard(order)
            self.ids.order_list.add_widget(card)
    
    def go_back(self):
        self.manager.current = 'profile'
    
    def open_cart(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'cart'

class OrderCard(MDCard):
    def __init__(self, order_data, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = "12dp"
        self.spacing = "10dp"
        self.radius = [15]
        self.elevation = 4
        self.size_hint = (None, None)
        self.size = ("350dp", "200dp")
        self.pos_hint = {"center_x": 0.5}

        # Order header
        header = MDBoxLayout(orientation='horizontal')
        header.add_widget(MDLabel(
            text=f"Order #{order_data['id']}",
            font_style="H6"
        ))
        header.add_widget(MDLabel(
            text=order_data['status'],
            theme_text_color="Custom",
            text_color=order_data['color']
        ))
        self.add_widget(header)

        # Order details
        details = MDBoxLayout(orientation='vertical', spacing=5)
        details.add_widget(MDLabel(text=f"Date: {order_data['date']}"))
        details.add_widget(MDLabel(text=f"Item: {order_data['item']}"))
        self.add_widget(details)

        # Action buttons
        actions = MDBoxLayout(orientation='horizontal', spacing=10)
        actions.add_widget(MDRaisedButton(
            text="View Details",
            on_release=lambda x: self.show_order_details(order_data)
        ))
        actions.add_widget(MDRaisedButton(
            text="Reorder",
            on_release=lambda x: self.reorder(order_data)
        ))
        self.add_widget(actions)
    
    def show_order_details(self, order_data):
        # TODO: Implement order details view
        print(f"Showing details for order {order_data['id']}")
    
    def reorder(self, order_data):
        # TODO: Implement reorder functionality
        print(f"Reordering {order_data['item']}")
