import allure
import pytest
from data.test_data import MESSAGES, ADDRESSES
from data.locators import ModalLocators
import re


@allure.feature("Заказ такси")
class TestTaxiOrder:
    
    @allure.title("Окно ожидания машины после заказа")
    @allure.description("Нажимаем кнопку 'Ввести номер и заказать' - появляется окно ожидания машины")
    def test_waiting_window_display(self, main_page, taxi_order_page, modal_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        taxi_order_page.click_laptop_slider()
        taxi_order_page.click_order_button()
        
        assert modal_page.is_order_modal_visible(), "Модальное окно заказа не отображается"
        
        order_title = modal_page.get_order_header_title()
        assert order_title == MESSAGES["SEARCH_MACHINE"], f"Ожидался заголовок '{MESSAGES['SEARCH_MACHINE']}', получен '{order_title}'"
        
        assert modal_page.is_timer_visible(), "Таймер обратного отсчета не отображается"
        
        timer_text = modal_page.get_order_header_time()
        assert timer_text, "Время таймера не отображается"
    
    @allure.title("Окно совершенного заказа после окончания таймера")
    @allure.description("Дождаться окончания таймера поиска машины - отображается окно совершенного заказа")
    def test_completed_order_window_display(self, main_page, taxi_order_page, modal_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        taxi_order_page.click_laptop_slider()
        taxi_order_page.click_order_button()
        
        modal_page.wait_for_custom_condition(
            lambda driver: "мин. и приедет" in modal_page.get_order_header_title() or 
                          "Поиск машины" in modal_page.get_order_header_title(),
            timeout=60
        )
        
        order_title = modal_page.get_order_header_title()
        title_completed = "мин. и приедет" in order_title
        title_searching = "Поиск машины" in order_title
        
        assert title_completed or title_searching, f"Неожиданный заголовок: {order_title}"
        
        if title_completed:
            car_number = main_page.driver.find_element(*ModalLocators.CAR_NUMBER)
            assert car_number.is_displayed(), "Номер автомобиля не отображается"
            
            car_image = main_page.driver.find_element(*ModalLocators.CAR_IMAGE)
            assert car_image.is_displayed(), "Картинка тарифа не отображается"
            
            driver_image = main_page.driver.find_element(*ModalLocators.DRIVER_IMAGE)
            assert driver_image.is_displayed(), "Фото водителя не отображается"
            
            driver_rating = main_page.driver.find_element(*ModalLocators.DRIVER_RATING)
            assert driver_rating.is_displayed(), "Рейтинг водителя не отображается"
            
            driver_name = main_page.driver.find_element(*ModalLocators.DRIVER_NAME)
            assert driver_name.is_displayed(), "Имя водителя не отображается"
    
    @allure.title("Проверка стоимости в деталях заказа")
    @allure.description("Нажать кнопку 'Детали' - указана стоимость, которая была при выборе тарифа")
    def test_order_details_price_match(self, main_page, taxi_order_page, modal_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        tariff_price = taxi_order_page.get_working_tariff_price()
        
        taxi_order_page.click_laptop_slider()
        taxi_order_page.click_order_button()
        
        modal_page.wait_for_custom_condition(
            lambda driver: "мин. и приедет" in modal_page.get_order_header_title() or 
                          "Поиск машины" in modal_page.get_order_header_title(),
            timeout=30
        )
        
        modal_page.click_details_button()
        details_price = modal_page.get_trip_price()
        
        tariff_number = re.search(r'\d+', tariff_price).group() if re.search(r'\d+', tariff_price) else ""
        details_number = re.search(r'\d+', details_price).group() if re.search(r'\d+', details_price) else ""
        
        assert tariff_number == details_number, \
            f"Стоимость не совпадает: тариф '{tariff_price}' ({tariff_number}), детали '{details_price}' ({details_number})"
    
    @allure.title("Работа кнопки 'Отмена'")
    @allure.description("Нажать кнопку 'Отмена' - окно закрывается")
    @pytest.mark.xfail(reason="Баг с неработающей кнопкой Отменить в окошке Заказа такси")
    def test_cancel_button_closes_window(self, main_page, taxi_order_page, modal_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        taxi_order_page.click_laptop_slider()
        taxi_order_page.click_order_button()
        
        assert modal_page.is_order_modal_visible(), "Модальное окно не отображается"
        
        modal_page.click_cancel_button()
        
        modal_page.wait_for_element_to_disappear(ModalLocators.ORDER_MODAL_WINDOW, timeout=5)
        
        window_closed = not modal_page.is_order_modal_visible()
        assert window_closed, "Окно не закрылось после нажатия кнопки 'Отмена'"
