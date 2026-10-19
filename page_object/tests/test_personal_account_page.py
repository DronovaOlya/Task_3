import allure
from page_object.locators.personal_account_page_locators import PersonalAccountPageLocators

@allure.epic('Личный кабинет')
class TestPersonalAccountPage:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_transition_personal_account(self, auth_user, main_page, personal_account_page):
        main_page.click_personal_account_button()

        check = personal_account_page.wait_and_find_element(PersonalAccountPageLocators.LOCATOR_PROFILE)
        assert check.is_displayed()

    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_order_history(self, auth_user, main_page, personal_account_page):
        main_page.click_personal_account_button()
        personal_account_page.click_order_history_button()
        
        check = personal_account_page.wait_and_find_element(PersonalAccountPageLocators.LOCATOR_HISTORY_ORDERS)
        assert check.is_displayed()

    @allure.title('Проверка выхода из аккаунта.')
    def test_apartment_exit(self, auth_user, main_page, personal_account_page):
        main_page.click_personal_account_button()
        personal_account_page.click_exit_button()
            
        check = personal_account_page.wait_and_find_element(PersonalAccountPageLocators.LOCATOR_BUTTON_ENTRANCE)
        assert check.is_displayed()

