import pytest
from selenium import webdriver
from page_object.pages.main_page import MainPage
from page_object.pages.order_feed_page import OrderFeedPage
from page_object.pages.password_page import PasswordPage
from page_object.pages.personal_account_page import PersonalAccountPage
from page_object.urls import URL_MAIN_PAGE
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from page_object.pages.main_page import MainPage
from page_object.locators.main_page_locators import MainPageLocators
import allure
from page_object.helpers import get_or_create_test_user



@pytest.fixture(params=["chrome", "firefox"])
def browser_name(request):
    return request.param

@pytest.fixture(scope="function")
def driver(browser_name):
    if browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("dom.webdriver.enabled", False)
        firefox_options.set_preference("browser.startup.homepage_override.mstone", "")
        firefox_options.set_preference("dom.drag_and_drop", True)
        browser = webdriver.Firefox(options=firefox_options)
    elif browser_name == "chrome":
        chrome_options = ChromeOptions()
        prefs = {"profile.password_manager_leak_detection": False}
        chrome_options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    return page

@pytest.fixture
def password_page(driver):
    page = PasswordPage(driver)
    return page

@pytest.fixture
def personal_account_page(driver):
    page = PersonalAccountPage(driver)
    return page

@pytest.fixture(scope="session")
def test_user():
    return get_or_create_test_user()

@allure.title('Авторизация')
@pytest.fixture
def auth_user(main_page, personal_account_page, test_user):
    main_page.go_to_page(URL_MAIN_PAGE)
    main_page.click_personal_account_button()
    personal_account_page.add_input_email(test_user['email'])
    personal_account_page.add_input_password(test_user['password'])
    personal_account_page.click_entrance_button()
    main_page.find_element_auth()

@allure.title('Создать заказ')
@pytest.fixture
def creat_order(main_page):
    main_page.go_to_page(URL_MAIN_PAGE)
    main_page.wait_and_find_element(MainPageLocators.LOCATOR_INGREDIENT_BUNS)
    main_page.add_bun_order()
    main_page.wait_and_find_element(MainPageLocators.LOCATOR_INGREDIENT_SAUSES)
    main_page.add_sauce_order()
    main_page.wait_and_find_element(MainPageLocators.LOCATOR_INGREDIENT_FILLINGS)
    main_page.add_filling_order()
    main_page.wait_and_find_element(MainPageLocators.LOCATOR_BUTTON_PLACE_ORDER)
    main_page.click_plase_order_button()
    
