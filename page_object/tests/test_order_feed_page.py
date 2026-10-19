import allure
from page_object.locators.order_feed_page_locators import OrderFeedPageLocators


@allure.epic('Проверка раздела "Лента заказов"')
class TestOrderFeedPage:
    @allure.title('Проверка всплывающего окна с деталями заказа')
    def test_order_details(self, auth_user, main_page, personal_account_page, order_feed_page):
        main_page.click_personal_account_button()
        personal_account_page.click_order_history_button()
        order_feed_page.click_order()

        check = order_feed_page.wait_and_find_element(OrderFeedPageLocators.LOCATOR_ORDER_COMPOSITION)
        assert check.is_displayed()

    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_feed_history_order(self, auth_user, creat_order, main_page, personal_account_page, order_feed_page):
        main_page.click_button_exit_order()
        main_page.click_personal_account_button()
        personal_account_page.click_order_history_button()
        number_order_hisrory = order_feed_page.number_order_history()
        order_feed_page.click_order_feed_button()
        numbers_order_feed_orders = order_feed_page.get_all_order_numbers_from_feed()

        assert number_order_hisrory in numbers_order_feed_orders

    @allure.title('Проверка увелечения счётчика "Выполнено за всё время" после офрмеления заказа')
    def test_counter_all_time(self, auth_user, main_page, order_feed_page):
        main_page.click_order_feed_button()
        before = order_feed_page.get_counter_all_time()
        main_page.click_designer_button()
        main_page.add_bun_order()
        main_page.add_sauce_order()
        main_page.add_filling_order()
        main_page.click_plase_order_button()
        main_page.click_button_exit_order()
        main_page.click_order_feed_button()

        after = order_feed_page.get_counter_all_time()
        assert after == before + 1

    @allure.title('Проверка увелечения счётчика "Выполнено за сегодня" после офрмеления заказа')
    def test_counter_today(self, auth_user, main_page, order_feed_page):
        main_page.click_order_feed_button()
        before = order_feed_page.get_counter_today()
        main_page.click_designer_button()
        main_page.add_bun_order()
        main_page.add_sauce_order()
        main_page.add_filling_order()
        main_page.click_plase_order_button()
        main_page.click_button_exit_order()
        main_page.click_order_feed_button()
        
        after = order_feed_page.get_counter_today()
        assert after == before + 1

    @allure.title('Проверка появления номера заказа в разделе "Готовы" после оформления заказа')
    def test_order_ready(self, auth_user, creat_order, order_feed_page, main_page):
        number_order = order_feed_page.number_order()
        number_digits = ''.join(filter(str.isdigit, number_order)).zfill(5)
        main_page.click_button_exit_order()
        main_page.click_order_feed_button()
        order_feed_page.wait_order_ready(number_digits)
        numbers = order_feed_page.get_order_numbers_ready()

        assert number_digits in numbers

   

