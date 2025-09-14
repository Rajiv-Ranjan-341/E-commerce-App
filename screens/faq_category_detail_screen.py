from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

class FAQCategoryDetailScreen(MDScreen):
    category_title = StringProperty("Category")



    def on_pre_enter(self, *args):
        self.populate_panels()

    def populate_panels(self):
        panel_box = self.ids.panel_box
        panel_box.clear_widgets()
        for faq in self.faqs:
            content = MDBoxLayout(orientation='vertical', adaptive_height=True, padding=("8dp", "8dp", "8dp", "8dp"))
            answer_label = MDLabel(
                text=faq['answer'],
                halign='left',
                theme_text_color='Secondary',
                size_hint_y=None
            )
            answer_label.height = answer_label.texture_size[1]
            answer_label.bind(
                texture_size=lambda instance, value: setattr(instance, 'height', value[1])
            )
            content.add_widget(answer_label)
            panel = MDExpansionPanel(
                content=content,
                panel_cls=MDExpansionPanelOneLine(text=faq['question'])
            )
            panel_box.add_widget(panel)

    def go_back(self):
        self.manager.current = 'FAQ' 