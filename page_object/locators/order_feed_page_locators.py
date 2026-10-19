from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    
    LOCATOR_ORDER =  By.XPATH, "//*[@class='OrderHistory_link__1iNby'][1]"  
    
    LOCATOR_COUNTER_ORDER_ALL_TIME = By.XPATH, "//p[contains(text(),'Выполнено за все время')]" "/following-sibling::p[contains(@class,'OrderFeed_number')]"
    
    LOCATOR_COUNTER_ORDER_TODAY = By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]" "/following-sibling::p[contains(@class,'OrderFeed_number')]"
   
    LOCATOR_ORDER_READY = By.XPATH, "//*[@class='OrderFeed_orderList__cBvyi']"

    LOCATOR_NUMBER_ORDER_HISTORY = By.XPATH, "(//p[contains(@class,'text_type_digits-default') and starts-with(text(),'#')])[last()]"

    LOCATOR_NUMBER_ORDER = By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]"
    
    LOCATOR_ORDERS = By.XPATH, ".//p[contains(@class,'text text_type_digits-default')][starts-with(text(),'#')]"

    LOCATOR_ORDER_COMPOSITION = By.XPATH, "//*[@class='text text_type_main-medium mb-8' and text()='Cостав']"
    
    