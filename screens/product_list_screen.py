from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty
from widgets.product_card import ProductCard
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.app import App
from functools import partial

Factory.register('ProductCard', module='widgets.product_card')
Builder.load_file('widgets/product_card.kv')

class ProductListScreen(MDScreen):
    products = ListProperty([
        # Herbal oils & Legiyams
        {
            'name': 'Sathuragiri Joint Pain Thailam 60g',
            'category': 'Herbal Oils & Legiyams',
            'price': '₹300',
            'image': 'assets/herbal oils/2.jpg',  
            'images': ['assets/herbal oils/2.jpg'],
            'description': 'Anti-inflammatory, soothes joints, lubricates and strengthens muscles'
        },
        {
            'name': 'Karisalankanni Oil 90g',
            'category': 'Herbal Oils & Legiyams',
            'price': '₹300',
            'image': 'assets/herbal oils/7.png',  
            'images': ['assets/herbal oils/7.png'],
            'description': 'Herbal oil for hair health; popular top-seller'
        },
        {
            'name': 'Karisalankanni Oil 180ml',
            'category': 'Herbal Oils & Legiyams',
            'price': '₹400',
            'image': 'assets/herbal oils/7.png',  # Placeholder image
            'images': ['assets/herbal oils/7.png'],
            'description': 'Larger bottle of the same nourishing hair oil'
        },
        {
            'name': 'Karunjeeragam Oil 50ml',
            'category': 'Herbal Oils & Legiyams',
            'price': '₹180',
            'image': 'assets/herbal oils/6.jpg',  # Placeholder image
            'images': ['assets/herbal oils/6.jpg'],
            'description': 'Herbal oil made from black cumin seeds'
        },
        {
            'name': 'Prasava Legiyam 500g',
            'category': 'Herbal Oils & Legiyams',
            'price': '₹220',
            'image': 'assets/herbal oils/8.jpg',  # Placeholder image
            'images': ['assets/herbal oils/8.jpg'],
            'description': 'Post-partum tonic for anemia, edema, vomiting; strengthens uterus'
        },
        {
            'name': 'Kaayakalpaa Kit',
            'category': 'Herbal oils & Legiyams',
            'price': '₹3,599',
            'image': 'assets/herbal oils/1.png',
            'images': ['assets/herbal oils/1.png'],
            'description': 'A rejuvenating herbal kit for daily wellness and vitality.'
        },
        {
            'name': 'Pure Karisalankanni Oil 225ml',
            'category': 'Herbal oils & Legiyams',
            'price': '₹2,120.00',
            'image': 'assets/herbal oils/7.png',
            'images': ['assets/herbal oils/7.png', 'assets/herbal oils/7.png', 'assets/herbal oils/7.png'],
            'description': (
                "This oil comes from a plant known in English as 'false daisy.' The herb is in the sunflower family and grows best in moist places including Thailand, India, and Brazil.\n"
                "Preparation:\n"
                "STEP-1: Equal quantities of nallennai, cow's milk and the powder are taken.\n"
                "STEP-2: The leaves of Karisalankanni plant are grinded in a mixer.\n"
                "STEP-3: Nallennai and cow's milk are added to the powder acheived.\n"
                "STEP-4: Boiling the three (Karisalankanni, Nallennai, Cow's milk) for 20 minutes in a stove. Thus, Karisalankanni oil is prepared."
            )
        },
        {
            'name': 'Eucalyptus Oil',
            'category': 'Herbal oils & Legiyams',
            'price': '₹200',
            'image': 'assets/herbal oils/4.jpg',
            'images': ['assets/herbal oils/4.jpg'],
            'description': 'Natural eucalyptus oil for soothing relief and aromatherapy.'
        },
        #Weight Loss
        {
            'name': 'SPL. Arokiya Podi 225g',
            'category': 'Herbal oils',
            'price': '₹999',
            'image': 'assets/weight loss/2.png',
            'images': ['assets/weight loss/2.png'],
            'description': 'Helps digestion, reduces bloating, adding to routine that may aid weight loss'
        },
        {
            'name': 'Thiribala Podi / Triphala Powder',
            'category': 'Herbal oils',
            'price': '',
            'image': 'assets/weight loss/3.jpg',
            'images': ['assets/weight loss/3.jpg'],
            'description': 'Natural colon cleanser that assists detox and slimming processes'
        },
        {
            'name': 'Karunjeeragam (Black cumin) 100g',
            'category': 'Herbal oils',
            'price': '₹50 (from ₹60)',
            'image': 'assets/weight loss/4.jpg',
            'images': ['assets/weight loss/4.jpg'],
            'description': 'Black cumin seeds promote weight loss, reduce diabetes risk, improve metabolism, enhance heart and digestive health, and support sexual wellness.'
        },
    #   Baby Care
        {
            'name': 'Kaasi Katti (10g)',
            'category': 'Baby Care',
            'price': '₹30',
            'image': 'assets/baby care images/5.jpg',
            'images': ['assets/baby care images/5.jpg'],
            'description': 'Traditional herbal chunk used for baby care—specific benefits not detailed.'
        },
        {
            'name': 'Black Bindi for Babies (1 piece)',
            'category': 'Baby Care',
            'price': '₹100',
            'image': 'assets/baby care images/13.jpg',
            'images': ['assets/baby care images/13.jpg'],
            'description': 'Protective black dot applied on baby\'s forehead to ward off negative energy; safe with no skin allergies'
        },
        {
            'name': 'Pillaivalathi Leaf (20g)',
            'category': 'Baby Care',
            'price': '₹100',
            'image': 'assets/baby care images/8.jpg',
            'images': ['assets/baby care images/8.jpg'],
            'description': 'Herbal leaf for baby use—detailed benefits not provided in listing.'
        },
        {
            'name': 'Vasambu Bangle (1 piece)',
            'category': 'Baby Care',
            'price': '₹60',
            'image': 'assets/baby care images/12.jpg',
            'images': ['assets/baby care images/12.jpg'],
            'description': 'A vasambu (sweetflag) root bracelet to calm babies, aid digestion, improve sleep, and offer protection'
        },
        {
            'name': 'Muligai Saampirani Set (100g)',
            'category': 'Baby Care',
            'price': '₹120',
            'image': 'assets/baby care images/9.jpg',
            'images': ['assets/baby care images/9.jpg'],
            'description': 'Herbal incense/resin set; baby-centric uses not explicitly described on listing.'
        },
        {
            'name': 'Spiked Ginger Lily (100g)',
            'category': 'Baby Care',
            'price': '₹120',
            'image': 'assets/baby care images/2.jpg',
            'images': ['assets/baby care images/2.jpg'],
            'description': 'Dried rhizome (Poolankizhangu); typically used for digestive and calming purposes in infants.'
        },
        {
            'name': 'Urasu / Orasu Medicine (1 set)',
            'category': 'Baby Care',
            'price': '₹60',
            'image': 'assets/baby care images/7.jpg',
            'images': ['assets/baby care images/7.jpg'],
            'description': 'Traditional herbal remedy ("orasu") made for infants; exact usage not specified.'
        },
        {
            'name': 'Kaadhola / Kaadholai Karugamani (1 set)',
            'category': 'Baby Care',
            'price': '₹60',
            'image': 'assets/baby care images/4.jpg',
            'images': ['assets/baby care images/4.jpg'],
            'description': 'Herbal thorn-berry remedy ("karugamani"); intended for baby wellness but specific benefits not listed.'
        },
        {
            'name': 'Vasambu / Sweetflag (2 pieces)',
            'category': 'Baby Care',
            'price': '₹20',
            'image': 'assets/baby care images/11.jpg',
            'images': ['assets/baby care images/11.jpg'],
            'description': 'Raw vasambu sticks commonly used as natural teething aids, to support digestion, and soothe ailments.'
        },
        {
            'name': 'Baby Care Combo (1 set)',
            'category': 'Baby Care',
            'price': '₹550',
            'image': 'assets/baby care images/1.jpg',
            'images': ['assets/baby care images/1.jpg'],
            'description': 'A curated combo containing Orasu Marundhu, Paalkayam, Kadukkai, Jathikkai, Maasakkai, Vasambu, and Kaadhola Karugamani—formulated for infants\' overall health.'
        },
           
    # Sugar
        {
            'name': 'Thean Kaai 50g ',
            'category': 'Sugar',
            'price': '₹80',
            'image': 'assets/sugar/7.jpg',
            'images': ['assets/sugar/7.jpg'],
            'description': 'Promotes digestion and helps regulate blood sugar levels'
        },
        {
            'name': 'Sirukurinjaan Powder ',
            'category': 'Sugar',
            'price': '₹50',
            'image': 'assets/sugar/5.jpg',
            'images': ['assets/sugar/5.jpg'],
            'description': 'Promotes digestion and helps regulate blood sugar levels'
        },
        {
            'name': 'Aavaarampoo Powder 50g ',
            'category': 'Sugar',
            'price': '₹30',
            'image': 'assets/sugar/3.jpg',
            'images': ['assets/sugar/3.jpg'],
            'description': 'Promotes digestion and helps regulate blood sugar levels'
        },
        {
            'name': 'Naaval Seed Powder 50g',
            'category': 'Sugar',
            'price': '₹9',
            'image': 'assets/sugar/6.jpg',
            'images': ['assets/sugar/6.jpg'],
            'description': 'Used traditionally to manage blood sugar, support heart health, and purification.'
        },
    #Stomach Pain
        {
            'name': 'Paalkaayam 50g',
            'category': 'Stomach Pain',
            'price': '₹40',
            'image': 'assets/stomach pain/5.jpg',
            'images': ['assets/stomach pain/5.jpg'],
            'description': 'Gentle herbal laxative—cleanses colon and aids digestion & weight management.'
        },
         {
            'name': 'Ajeeranaa Powder 225g',
            'category': 'Stomach Pain',
            'price': '₹625',
            'image': 'assets/stomach pain/6.png',
            'images': ['assets/stomach pain/6.png'],
            'description': 'Gentle herbal laxative—cleanses colon and aids digestion & weight management.'
        },
         {
            'name': 'Attathi Powder 50g',
            'category': 'Stomach Pain',
            'price': '₹80',
            'image': 'assets/stomach pain/7.jpg',
            'images': ['assets/stomach pain/7.jpg'],
            'description': 'Gentle herbal laxative—cleanses colon and aids digestion & weight management.'
        },
     # Rice & Millets
        {
            'name': 'Scool Rice 50g',
            'category': 'Millets & Rice',
            'price': '₹80',
            'image': 'assets/rice/2.jpg',
            'images':  ['assets/rice/2.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
         {
            'name': 'Popcorn Sorghum 100g',
            'category': 'Millets & Rice',
            'price': '₹15',
            'image': 'assets/rice/3.jpg',
            'images':  ['assets/rice/3.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
          {
            'name': 'Aali Rice 50g',
            'category': 'Millets & Rice',
            'price': '₹25',
            'image': 'assets/rice/4.jpg',
            'images':  ['assets/rice/4.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
          {
            'name': 'Maapillai Samba Rice 100g',
            'category': 'Millets & Rice',
            'price': '₹15',
            'image': 'assets/rice/5.jpg',
            'images':  ['assets/rice/5.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
        {
            'name': 'Little Millet / Saamai Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹10',
            'image': 'assets/rice/6.jpg',
            'images':  ['assets/rice/6.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
         {
            'name': 'Kaikutthal Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹15',
            'image': 'assets/rice/7.jpg',
            'images':  ['assets/rice/7.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
        {
            'name': 'Kudhiraivali Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹15',
            'image': 'assets/rice/8.jpg',
            'images':  ['assets/rice/8.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
        {
            'name': 'Varau Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹15',
            'image': 'assets/rice/9.jpg',
            'images':  ['assets/rice/9.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
        {
            'name': 'Thinai Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹15',
            'image': 'assets/rice/10.jpg',
            'images':  ['assets/rice/10.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
        {
            'name': 'Forbidden Rice 100g',
            'category': 'Millets & Rice',
            'price': '₹25',
            'image': 'assets/rice/11.jpg',
            'images':  ['assets/rice/11.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
          {
            'name': 'pumpkin Seeds 100g',
            'category': 'Millets & Rice',
            'price': '₹99',
            'image': 'assets/rice/12.jpg',
            'images':  ['assets/rice/12.jpg'],
            'description': 'Small-grain millet valued for its fiber content and low glycemic impact.'
        },
          {
            'name': 'Sivappu Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹10 ',
            'image': 'assets/rice/13.jpg',
            'images': ['assets/rice/13.jpg'] ,
            'description': 'Unpolished red rice packed with fiber, vitamins B1/B2, iron, antioxidants—promotes heart health, blood sugar management, and weight control.'
        },
        {
            'name': 'Solam / Sorghum 100g',
            'category': 'Millets & Rice',
            'price': '₹10',
            'image': 'assets/rice/20.jpg' ,
            'description': 'A high-fiber millet alternative to refined flour, rich in protein, iron, potassium, and phosphorus—supports digestion, weight management, cholesterol control, and heart health.'
        },
        {
            'name': 'Bamboo Rice/Moongil Arisi 100g',
            'category': 'Millets & Rice',
            'price': '₹80 ',
            'image': 'assets/rice/18.jpg',
            'images':  ['assets/rice/18.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
       #sex life
       {
            'name': 'Murungai Vithai Powder 50g',
            'category': 'sex life',
            'price': '₹90 ',
            'image': 'assets/sex ife/3.jpg',
            'images':  ['assets/sex ife/3.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
        {
            'name': 'Oridhazh Thamarai Powder 50g',
            'category': 'sex life',
            'price': '₹40 ',
            'image': 'assets/sex ife/4.jpg',
            'images':  ['assets/sex ife/4.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
        {
            'name': 'Drumstick Flower Powder 50g',
            'category': 'sex life',
            'price': '₹90 ',
            'image': 'assets/sex ife/6.jpg',
            'images':  ['assets/sex ife/6.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
        {
            'name': 'Poonaikaali Seed Powder 50g',
            'category': 'sex life',
            'price': '₹80 ',
            'image': 'assets/sex ife/7.jpg',
            'images':  ['assets/sex ife/7.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
        {
            'name': 'Kadal Paasi 50g',
            'category': 'sex life',
            'price': '₹50 ',
            'image': 'assets/sex ife/8.jpg',
            'images':  ['assets/sex ife/8.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
        {
            'name': 'Black Musli Powder 50g',
            'category': 'sex life',
            'price': '₹60 ',
            'image': 'assets/sex ife/9.jpg',
            'images':  ['assets/sex ife/9.jpg'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
       
         {
            'name': 'Atthipalam',
            'category': 'sex life',
            'price': '₹2,000 ',
            'image': 'assets/sex ife/12.png',
            'images':  ['assets/sex ife/12.png'],
            'description': 'Nutty, aromatic rice harvested from bamboo inflorescence—rich in nutrients, traditionally used in festive dishes.'
        },
    ])

    def on_pre_enter(self, *args):
        print("on_pre_enter called")  # DEBUG
        """
        Called before the screen is displayed.
        Initializes or syncs the wishlist state with the app's persistent wishlist,
        and populates the product grid.
        """
        app = App.get_running_app()
        # Ensure wishlist is initialized as a list
        if not hasattr(app, 'wishlist'):
            app.wishlist = []
        self.show_products(self.products)
        # Bind search bar events
        search_input = self.ids.get('search_input')
        if search_input:
            search_input.bind(text=self.on_search_text)
            search_input.bind(on_text_validate=self.on_search_enter)

    def on_leave(self, *args):
        # Unbind search bar events to avoid duplicate bindings
        search_input = self.ids.get('search_input')
        if search_input:
            search_input.unbind(text=self.on_search_text)
            search_input.unbind(on_text_validate=self.on_search_enter)

    def on_search_text(self, instance, value):
        if value.strip() == '':
            self.reset_product_filter()
        else:
            self.filter_products_by_search(value)

    def on_search_enter(self, instance):
        value = instance.text
        self.filter_products_by_search(value)

    def show_products(self, products_to_show=None):
        search_input = self.ids.get('search_input')
        if search_input:
            search_input.focus = False
        """
        Populates the product grid with a given list of products. If None, shows all products.
        """
        app = App.get_running_app()
        grid = self.ids.product_grid
        grid.clear_widgets()
        grid.cols = 2
        products = products_to_show if products_to_show is not None else self.products
        for product in products:
            idx = self.products.index(product)
            # Check if product is in wishlist by name
            is_favorite = any(item['name'] == product['name'] for item in app.wishlist)
            card = ProductCard(
                image=product['image'],
                name=product['name'],
                category=product.get('category', ''),
                price=product['price'],
                is_favorite=is_favorite,
                on_favorite_toggle=self.make_favorite_callback(idx)
            )
            card.on_press_callback = partial(self.open_product_details, product)
            # print("on_press_callback for", product['name'], "is", card.on_press_callback)  # DEBUG
            grid.add_widget(card)

    def filter_products_by_search(self, search_text):
        """
        Filters products by search text and displays them in the product grid.
        """
        search_text = search_text.strip().lower()
        if not search_text:
            self.show_products(self.products)
            return
        filtered = [p for p in self.products if search_text in p['name'].lower() or search_text in p['category'].lower()]
        self.show_products(filtered)

    def reset_product_filter(self):
        self.show_products(self.products)

    def make_favorite_callback(self, idx):
        return lambda card, fav: self.toggle_wishlist(idx, fav)

    def toggle_wishlist(self, idx, is_favorite):
        # print(f"toggle_wishlist called for idx={idx}, is_favorite={is_favorite}")  # DEBUG
        app = App.get_running_app()
        product = self.products[idx]
        
        if is_favorite:
            # Add to wishlist
            wishlist_item = {
                'name': product['name'],
                'image': product['image'],
                'price': product['price'],
                'category': product.get('category', '')
            }
            # Check if already in wishlist
            if not any(item['name'] == product['name'] for item in app.wishlist):
                app.wishlist.append(wishlist_item)
        else:
            # Remove from wishlist
            app.wishlist = [item for item in app.wishlist if item['name'] != product['name']]
        
        print(f"Wishlist after toggle: {app.wishlist}")  # DEBUG
        """
        Toggles the wishlist status for a product at the given index.
        Updates the app-level wishlist, and refreshes the grid.
        """
        self.show_products()

    def go_back(self):
        """
        Navigates back to the home screen.
        """
        app = App.get_running_app()
        app.root.current = 'home'

    def remove_from_wishlist_by_name(self, product_name):
        """
        Removes a product from the wishlist by its name.
        Removes the item from the app's wishlist and updates the display.
        """
        app = App.get_running_app()
        app.wishlist = [item for item in app.wishlist if item['name'] != product_name]
        self.show_products()

    def open_cart(self):
        app = App.get_running_app()
        app.last_screen = self.manager.current_screen.name
        self.manager.current = 'cart' 

    def open_product_details(self, product, *args):
        print(f"Opening details for {product['name']}")  # DEBUG
        app = App.get_running_app()
        app.last_screen = self.manager.current
        details_screen = app.sm.get_screen('product_details')
        details_screen.set_product(
            name=product['name'],
            price=float(product['price'].replace('₹','').replace(',','').replace('.00','')) if isinstance(product['price'], str) else product['price'],
            images=product.get('images', [product.get('image', '')]),
            description=product.get('description', 'No description available.'),
            category=product.get('category', '')
        )
        app.sm.current = 'product_details' 