import allure
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage
from page_object.helpers import get_random_bun, get_random_sauce, get_random_filling

class MainPage(BasePage):
    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_PERSONAL_ACCOUNT)
     
    @allure.step('Нажать на кнопку "Конструктор"')
    def click_designer_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_DESIGNER)
    
    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_ORDER_FEED)

    @allure.step('Нажать на ингредиент')
    def click_ingredient_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_INGREDIENT_BUNS)

    @allure.step('Нажать на кнопку закрытия деталей заказа')
    def click_exit_ingredient_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_EXIT_INGREDIENT)

    @allure.step('Перетянуть ингредиент в заказ')
    def add_ingredient_order(self):
        locator_to = MainPageLocators.LOCATOR_CONSTRUCTOR_ELEMENTS
        locator_from = MainPageLocators.LOCATOR_INGREDIENT_SAUSE
        self.drag_element_to(locator_from, locator_to)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_plase_order_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_PLACE_ORDER)

    @allure.step('Найти элемент')
    def find_element_auth(self):
        self.wait_and_find_element(MainPageLocators.LOCATOR_COLLECT_ORDER)

    @allure.step('Взять начальное значение каунтера')
    def get_counter(self) -> int:
        return self.get_counter_value(MainPageLocators.LOCATOR_COUNTER_SAUCE)

    def get_random_bun(self):
        return get_random_bun(self.driver)

    def get_random_sauce(self):
        return get_random_sauce(self.driver)

    def get_random_filling(self):
        return get_random_filling(self.driver)

    @allure.step('Перетянуть булку в заказ')
    def add_bun_order(self):
        bun = self.get_random_bun()
        self.drag_element_to(bun, MainPageLocators.LOCATOR_CONSTRUCTOR_ELEMENTS)
    
    @allure.step('Перетянуть соус в заказ')
    def add_sauce_order(self):
        sauce = self.get_random_sauce()
        self.drag_element_to(sauce, MainPageLocators.LOCATOR_CONSTRUCTOR_ELEMENTS)

    @allure.step('Перетянуть начинку в заказ')
    def add_filling_order(self):
        filling = self.get_random_filling()
        self.drag_element_to(filling, MainPageLocators.LOCATOR_CONSTRUCTOR_ELEMENTS)

    @allure.step('Нажать на кнопку закрыть после оформления заказ')
    def click_button_exit_order(self):
        self.click_to_element(MainPageLocators.LOCATOR_EXIT_ORDER)

    @allure.step('Взять номер заказа')
    def number_order(self):
        return self.get_text_to_element(MainPageLocators.LOCATOR_ORDER)