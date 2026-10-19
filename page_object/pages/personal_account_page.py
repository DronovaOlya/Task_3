import allure
from page_object.pages.base_page import BasePage
from page_object.locators.personal_account_page_locators import PersonalAccountPageLocators

class PersonalAccountPage(BasePage):
    @allure.step('Нажать на кнопку "История заказов"')
    def click_order_history_button(self):
        self.click_to_element(PersonalAccountPageLocators.LOCATOR_BUTTON_HISTORY_ORDERS)

    @allure.step('Нажать на кнопку "Выход"')
    def click_exit_button(self):
        self.click_to_element(PersonalAccountPageLocators.LOCATOR_BUTTON_EXIT)

    @allure.step('Заполнить поле "Email"')
    def add_input_email(self, email):
        self.add_text_to_element(PersonalAccountPageLocators.LOCATOR_INPUT_EMAIL, email)

    @allure.step('Заполнить поле "Пароль"')
    def add_input_password(self, password):
        self.add_text_to_element(PersonalAccountPageLocators.LOCATOR_INPUT_PASSWORD, password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_entrance_button(self):
        self.click_to_element(PersonalAccountPageLocators.LOCATOR_BUTTON_ENTRANCE)
    