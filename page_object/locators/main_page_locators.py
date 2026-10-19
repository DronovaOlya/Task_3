from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_BUTTON_PERSONAL_ACCOUNT = (By.XPATH,"//a[@href='/account'][contains(., 'Личный Кабинет')]")

    LOCATOR_BUTTON_DESIGNER = By.XPATH, "//*[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"

    LOCATOR_BUTTON_ORDER_FEED = By.XPATH, "//*[@class='undefined ml-2']"

    LOCATOR_INGREDIENT_BUNS = (By.XPATH,".//ul[contains(@class,'BurgerIngredients_ingredients__list__2A-mT')]" "/a[.//img[contains(@src,'bun-')]]")
    
    LOCATOR_INGREDIENT_SAUSE = By.XPATH, './/img[@src="https://code.s3.yandex.net/react/code/sauce-01.png"]'

    LOCATOR_EXIT_INGREDIENT = By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button']"
    
    LOCATOR_BUTTON_PLACE_ORDER = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']"
    
    LOCATOR_CONSTRUCTOR_ELEMENTS = By.XPATH, ".//span[@class='constructor-element__row']"
    
    LOCATOR_INGREDIENT_SAUSES = (By.XPATH,".//ul[contains(@class,'BurgerIngredients_ingredients__list__2A-mT')]""/a[.//img[contains(@src,'sauce-')]]")
    
    LOCATOR_INGREDIENT_FILLINGS = (By.XPATH, ".//a[contains(@class,'BurgerIngredient_ingredient')]""[.//img[not(contains(@src,'bun-')) and not(contains(@src,'sauce-'))]]")
    
    LOCATOR_EXIT_ORDER = By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button']"
    
    LOCATOR_ORDER =  By.XPATH, "//h2[contains(@class,'Modal_modal__title') and contains(@class,'text_type_digits-large')]"


    
    LOCATOR_COLLECT_ORDER = By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10' and text() ='Соберите бургер']"
    
    LOCATOR_ORDER_FEED = By.XPATH, ".//h1[@class='text text_type_main-large mt-10 mb-5' and text() ='Лента заказов']"
    
    LOCATOR_INGREDIENT_DETAILS = By.XPATH, ".//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10' and text() ='Детали ингредиента']"
    
    LOCATOR_COUNTER_SAUCE = By.XPATH,".//img[contains(@src,'sauce-01.png')]/preceding-sibling::div[contains(@class,'counter_counter')]//p"
    
    LOCATOR_PLACE_ORDER = By.XPATH, "//*[@class='undefined text text_type_main-medium mb-15' and text()='идентификатор заказа']"
    
    
    