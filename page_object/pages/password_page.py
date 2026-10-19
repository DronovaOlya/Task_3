import allure
from page_object.pages.base_page import BasePage
from page_object.locators.password_page_locators import PasswordPageLocators
from selenium.webdriver.support.ui import WebDriverWait


class PasswordPage(BasePage):
    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_reset_password(self):
        self.click_to_element(PasswordPageLocators.LOCATOR_BUTTON_RESTORE_PASSWORD)

    @allure.step('Ввести email"')
    def enter_email(self, data):
        self.add_text_to_element(PasswordPageLocators.LOCATOR_INPUT_EMAIL, data)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_restore_button(self):
        self.click_to_element(PasswordPageLocators.LOCATOR_BUTTON_RESTORE)

    @allure.step('Нажать на кнопку "Показать/скрыть пароль"')
    def click_show_password_button(self):
        self.click_to_element(PasswordPageLocators.LOCATOR_BUTTON_SEE_PASSWORD)

    @allure.step("Проверить, что рамка поля пароля стала активной (появился класс input_status_active)")
    def check_password_field_is_active(self):
        element = self.wait_and_find_element(PasswordPageLocators.LOCATOR_INPUT_PASSWORD)
        WebDriverWait(self.driver, 10).until(lambda d: "input_status_active" in element.get_attribute("class"))
        return True