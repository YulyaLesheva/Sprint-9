import allure
from pages.base_page import BasePage
from data.locators import ModalLocators


class ModalPage(BasePage):
    url = "https://ez-route.stand.praktikum-services.ru/"

    def is_order_modal_visible(self):
        with allure.step("Проверка видимости модального окна заказа"):
            return self.is_visible(ModalLocators.ORDER_MODAL_WINDOW)

    def get_order_header_title(self):
        with allure.step("Получение заголовка модального окна заказа"):
            return self.get_text(ModalLocators.ORDER_HEADER_TITLE)

    def get_order_header_time(self):
        with allure.step("Получение времени в заголовке модального окна"):
            return self.get_text(ModalLocators.ORDER_HEADER_TIME)

    def is_timer_visible(self):
        with allure.step("Проверка видимости таймера"):
            return self.is_visible(ModalLocators.ORDER_HEADER_TIME)

    def click_details_button(self):
        with allure.step("Клик по кнопке 'Детали'"):
            self.click(ModalLocators.DETAILS_BUTTON)

    def click_cancel_button(self):
        with allure.step("Клик по кнопке 'Отменить'"):
            self.click(ModalLocators.CANCEL_BUTTON)

    def get_trip_price(self):
        with allure.step("Получение стоимости поездки"):
            return self.get_text(ModalLocators.TRIP_PRICE)

    def get_car_number(self):
        with allure.step("Получение номера автомобиля"):
            return self.get_text(ModalLocators.CAR_NUMBER)

    def is_car_image_visible(self):
        with allure.step("Проверка видимости изображения автомобиля"):
            return self.is_visible(ModalLocators.CAR_IMAGE)

    def is_driver_image_visible(self):
        with allure.step("Проверка видимости изображения водителя"):
            return self.is_visible(ModalLocators.DRIVER_IMAGE)

    def get_driver_rating(self):
        with allure.step("Получение рейтинга водителя"):
            return self.get_text(ModalLocators.DRIVER_RATING)

    def get_driver_name(self):
        with allure.step("Получение имени водителя"):
            return self.get_text(ModalLocators.DRIVER_NAME) 