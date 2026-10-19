import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from page_object.helpers import wait_modal_overlay_closed


class BasePage:
    def __init__(self, driver, timeout=10, counter: int = 0 ):
        self.driver = driver
        self.timeout = timeout
        self.counter = counter 
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открыть главную страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент')
    def wait_and_find_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти элементы')
    def wait_and_find_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    def wait_modal_overlay_closed(self):
        return wait_modal_overlay_closed(self.driver)

    @allure.step('Нажать на элемент')
    def click_to_element(self, locator):
        self.wait_modal_overlay_closed()
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text

    @allure.step('Заполнить поле ввода')
    def add_text_to_element(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def get_text_to_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Перетащить элемент')
    def drag_element_to(self, locator_or_element, locator_to):
        element_to = self.wait_and_find_element(locator_to)
        if isinstance(locator_or_element, tuple):
            element_from = self.wait_and_find_element(locator_or_element)
        else:
            element_from = locator_or_element
            
        if self.driver.name == "firefox":
            script = """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
            """
            self.driver.execute_script(script, element_from, element_to)
        else:
            ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    @allure.step('Взять начальное значение счетчика')
    def get_counter_value(self, locator) -> int:
        return int(self.get_text_to_element(locator))

    @allure.step('Получить список номеров заказов')
    def get_numbers(self, locator):
        raw = self.get_text_to_element(locator)
        if isinstance(raw, list):
            raw = "\n".join(str(x) for x in raw)
        return [n.strip() for n in raw.split("\n") if n.strip()]

    


    
    