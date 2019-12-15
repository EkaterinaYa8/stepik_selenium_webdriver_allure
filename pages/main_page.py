from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_all_products_page(self):
        self.click_on_element(*MainPageLocators.ALL_PRODUCTS_LINK)
