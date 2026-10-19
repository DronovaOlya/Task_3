import allure
from page_object.locators.order_feed_page_locators import OrderFeedPageLocators
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait


class OrderFeedPage(BasePage):
    @allure.step('Нажать на заказ')
    def click_order(self):
        self.click_to_element(OrderFeedPageLocators.LOCATOR_ORDER)
    
    @allure.step('Взять номер заказа из Истории заказа')
    def number_order_history(self):
        return self.get_text_to_element(OrderFeedPageLocators.LOCATOR_NUMBER_ORDER_HISTORY)

    @allure.step('Взять номер созданного заказа')
    def number_order(self):
        WebDriverWait(self.driver, 30).until(lambda d: self.get_text_to_element(OrderFeedPageLocators.LOCATOR_NUMBER_ORDER) != '9999')
        return self.get_text_to_element(OrderFeedPageLocators.LOCATOR_NUMBER_ORDER)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_ORDER_FEED)

    @allure.step('Вернуть список номеров заказов из ленты')
    def get_all_order_numbers_from_feed(self) -> list[str]:
        elements = self.wait_and_find_elements(OrderFeedPageLocators.LOCATOR_ORDERS)
        return [el.text for el in elements]

    @allure.step('Взять начально значение счетчика за все время')
    def get_counter_all_time(self):
        return self.get_counter_value(OrderFeedPageLocators.LOCATOR_COUNTER_ORDER_ALL_TIME)

    @allure.step('Взять начально значение счетчика за сегодня')
    def get_counter_today(self):
            return self.get_counter_value(OrderFeedPageLocators.LOCATOR_COUNTER_ORDER_TODAY)

    @allure.step('Найти все готовые заказы')
    def number_order_progress(self) -> list[str]:
        elements = self.wait_and_find_elements(OrderFeedPageLocators.LOCATOR_ORDER_READY)
        return [el.text for el in elements]

    @allure.step('Получить номера заказов в разделе "Готовы"')
    def get_order_numbers_ready(self):
        return self.get_numbers(OrderFeedPageLocators.LOCATOR_ORDER_READY)

    @allure.step('Дождаться появления номера в разделе "Готовы"')
    def wait_order_ready(self, number):
        def order_appeared(driver):
            numbers = self.get_order_numbers_ready()
            return number in numbers
