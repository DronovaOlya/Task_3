import allure
from page_object.urls import URL_MAIN_PAGE
from page_object.locators.main_page_locators import MainPageLocators

@allure.epic('Проверка основного функционала')
class TestMainPage:
    @allure.title('Переход по клику на «Конструктор»')
    def test_navigation_constructor(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_personal_account_button()
        main_page.click_designer_button()

        check = main_page.wait_and_find_element(MainPageLocators.LOCATOR_COLLECT_ORDER)
        assert check.is_displayed()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_navigation_order_feed(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_order_feed_button()
    
        check = main_page.wait_and_find_element(MainPageLocators.LOCATOR_ORDER_FEED)
        assert check.is_displayed()

    @allure.title('Проверка всплывающего окно с деталями ингредиента') 
    def test_ingredient_details(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_ingredient_button()
        
        check = main_page.wait_and_find_element(MainPageLocators.LOCATOR_INGREDIENT_DETAILS)
        assert check.is_displayed()

    @allure.title('Закрытие всплывающего окно с деталями ингредиента') 
    def test_ingredient_details_exit(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.click_ingredient_button()
        main_page.click_exit_ingredient_button()
            
        check = main_page.wait_and_find_element(MainPageLocators.LOCATOR_COLLECT_ORDER)
        assert check.is_displayed()

    @allure.title('Добавление ингредиента в заказ и увеличивается каунтера данного ингредиента') 
    def test_add_ingredient_order(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        before = main_page.get_counter()
        main_page.add_ingredient_order()
        after = main_page.get_counter()

        assert after == before + 1

    @allure.title('Оформление заказа залогининным пользователем') 
    def test_place_order_auth_user(self, auth_user, main_page):
        main_page.add_bun_order()
        main_page.add_sauce_order()
        main_page.add_filling_order()
        main_page.click_plase_order_button()

        check = main_page.wait_and_find_element(MainPageLocators.LOCATOR_PLACE_ORDER)
        assert check.is_displayed()