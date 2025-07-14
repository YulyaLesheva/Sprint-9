import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.taxi_order_page import TaxiOrderPage
from pages.modal_page import ModalPage
from data.test_data import ADDRESSES


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
def taxi_order_page(driver):
    return TaxiOrderPage(driver)


@pytest.fixture
def modal_page(driver):
    return ModalPage(driver)


@pytest.fixture
def set_route(main_page):
    main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
    return main_page


@pytest.fixture
def set_same_route(main_page):
    main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_1"])
    return main_page
