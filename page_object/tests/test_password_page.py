import allure
from page_object.urls import URL_MAIN_PAGE
from page_object.locators.password_page_locators import PasswordPageLocators
from page_object.data import user_data


@allure.epic('Востановление пароля')
class TestPasswordPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recovery_page(self, password_page, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_personal_account_button()
        password_page.click_reset_password()

        check = password_page.wait_and_find_element(PasswordPageLocators.LOCATOR_INPUT_EMAIL)
        assert check.is_displayed()

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_button_recovery(self, password_page, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_personal_account_button()
        password_page.click_reset_password()
        password_page.enter_email(user_data["email"])
        password_page.click_restore_button()

        check = password_page.wait_and_find_element(PasswordPageLocators.LOCATOR_BUTTON_SAVE)
        assert check.is_displayed()

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_button_show_hide_password(self, password_page, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_personal_account_button()
        password_page.click_reset_password()
        password_page.enter_email(user_data["email"])
        password_page.click_restore_button()
        password_page.click_show_password_button()

        assert password_page.check_password_field_is_active()

        


