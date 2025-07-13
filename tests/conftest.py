import pytest
from selenium import webdriver

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()
    driver.get("https://ez-route.stand.praktikum-services.ru/")
    driver.maximize_window()
    
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def set_route(main_page):
    main_page.set_addresses("Хамовнический вал, 34", "Зубовский бульвар, 37")
    return main_page


@pytest.fixture
def set_same_route(main_page):
    main_page.set_addresses("Хамовнический вал, 34", "Хамовнический вал, 34")
    return main_page
