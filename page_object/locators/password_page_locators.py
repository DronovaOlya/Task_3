from selenium.webdriver.common.by import By

class PasswordPageLocators:
    
    LOCATOR_BUTTON_RESTORE_PASSWORD = By.XPATH, "//*[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
    
    LOCATOR_INPUT_EMAIL = By.CSS_SELECTOR, "input[name='name']"
    
    LOCATOR_BUTTON_RESTORE = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']"
    
    LOCATOR_BUTTON_SEE_PASSWORD = By.XPATH, ".//div[@class='input__icon input__icon-action']"

    LOCATOR_INPUT_PASSWORD = By.CSS_SELECTOR, "div.input__container div.input[class*='input_type_']"
   
    LOCATOR_BUTTON_SAVE = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Сохранить']"


