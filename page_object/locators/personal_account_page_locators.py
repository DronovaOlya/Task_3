from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    
    LOCATOR_BUTTON_HISTORY_ORDERS = By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and text()='История заказов']"
    
    LOCATOR_BUTTON_EXIT = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']"
    
    LOCATOR_INPUT_EMAIL = By.CSS_SELECTOR, "input[name='name']"

    LOCATOR_INPUT_PASSWORD = By.CSS_SELECTOR, "input[name='Пароль']"

    LOCATOR_HISTORY_ORDERS = By.XPATH, ".//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']"
    
    LOCATOR_BUTTON_ENTRANCE = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text() = 'Войти']"
    
    LOCATOR_PROFILE = By.XPATH, "//*[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='Профиль']"