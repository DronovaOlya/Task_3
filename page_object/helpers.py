import random
import json
import os
import requests
from selenium.webdriver.remote.webelement import WebElement
from page_object.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from page_object.data import USER_FILE, user_data
from page_object.urls import REGISTER_ENDPOINT

def get_random_bun(driver) -> WebElement:
    buns = driver.find_elements(*MainPageLocators.LOCATOR_INGREDIENT_BUNS)
    if not buns:
        raise AssertionError("Булки не найдены на странице")
    return random.choice(buns)

def get_random_sauce(driver) -> WebElement:
    sauces = driver.find_elements(*MainPageLocators.LOCATOR_INGREDIENT_SAUSES)
    if not sauces:
        raise AssertionError("Соусы не найдены на странице")
    return random.choice(sauces)

def get_random_filling(driver) -> WebElement:
    fillings = driver.find_elements(*MainPageLocators.LOCATOR_INGREDIENT_FILLINGS)
    if not fillings:
        raise AssertionError("Начинки не найдены на странице")
    return random.choice(fillings)

def wait_modal_overlay_closed(driver):
        overlay = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
        try:
            WebDriverWait(driver, 1).until(
                expected_conditions.visibility_of_element_located(overlay)
            )
            WebDriverWait(driver, 1).until(
                expected_conditions.invisibility_of_element_located(overlay)
            )
        except TimeoutException:
            pass


def get_or_create_test_user():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            user = json.load(f)
        return user
    requests.post(REGISTER_ENDPOINT, json=user_data)
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(user_data, f, ensure_ascii=False, indent=2)
    return user_data
