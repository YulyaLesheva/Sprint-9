import allure
from pages.base_page import BasePage
from data.locators import MainPageLocators, TaxiOrderLocators, ModalLocators


class MainPage(BasePage):
    url = "https://ez-route.stand.praktikum-services.ru/"

    # Работа с адресами
    def enter_from_address(self, address):
        with allure.step(f"Ввод адреса отправления: {address}"):
            self.type(MainPageLocators.FROM_INPUT, address)

    def enter_to_address(self, address):
        with allure.step(f"Ввод адреса назначения: {address}"):
            self.type(MainPageLocators.TO_INPUT, address)

    def set_addresses(self, from_address, to_address):
        with allure.step(f"Установка маршрута: {from_address} → {to_address}"):
            self.enter_from_address(from_address)
            self.enter_to_address(to_address)

    # Работа с видами маршрута
    def select_optimal_route(self):
        with allure.step("Выбор оптимального маршрута"):
            self.click(MainPageLocators.OPTIMAL_ROUTE)

    def select_mine_route(self):
        with allure.step("Выбор своего маршрута"):
            self.click(MainPageLocators.MINE_ROUTE)
    
    def select_fast_route(self):
        with allure.step("Выбор быстрого маршрута"):
            self.click(MainPageLocators.FAST_ROUTE)
    
    def is_route_mode_active(self):
        with allure.step("Проверка активности режима маршрута"):
            return self.is_visible(MainPageLocators.ACTIVE_MODE)
    
    def is_route_block_shown(self):
        with allure.step("Проверка отображения блока маршрута"):
            return self.is_visible(MainPageLocators.ROUTE_BLOCK_SHOWN)

    # Работа с типами передвижения
    def select_drive_type(self):
        with allure.step("Выбор типа передвижения: Драйв"):
            self.click(MainPageLocators.DRIVE_TYPE)
    
    def is_types_container_visible(self):
        with allure.step("Проверка видимости контейнера типов передвижения"):
            return self.is_visible(MainPageLocators.TYPES_CONTAINER)
    
    def get_active_types(self):
        with allure.step("Получение активных типов передвижения"):
            return self.find_elements(MainPageLocators.TYPES_ACTIVE)
    
    def get_disabled_types(self):
        with allure.step("Получение неактивных типов передвижения"):
            return self.find_elements(MainPageLocators.TYPES_DISABLED)
    
    def is_drive_type_available(self):
        with allure.step("Проверка доступности типа Драйв"):
            return self.is_visible(MainPageLocators.DRIVE_TYPE)

    # Кнопки действий
    def click_call_taxi_button(self):
        with allure.step("Клик по кнопке 'Вызвать такси'"):
            self.click(MainPageLocators.CALL_TAXI_BUTTON)

    def click_book_drive_button(self):
        with allure.step("Клик по кнопке 'Забронировать'"):
            self.click(MainPageLocators.BOOK_DRIVE_BUTTON)

    # Проверки видимости элементов
    def is_route_block_visible(self):
        with allure.step("Проверка видимости блока с выбором маршрута"):
            return self.is_visible(MainPageLocators.ROUTE_BLOCK)

    def is_route_points_visible(self):
        with allure.step("Проверка видимости точек маршрута на карте"):
            first_point = self.is_visible(MainPageLocators.WAYPOINT_FIRST)
            second_point = self.is_visible(MainPageLocators.WAYPOINT_SECOND)
            return first_point and second_point
    
    def get_route_points_general(self):
        with allure.step("Получение общих точек маршрута"):
            return self.find_elements(MainPageLocators.ROUTE_POINTS_GENERAL)

    def is_call_taxi_button_active(self):
        with allure.step("Проверка активности кнопки 'Вызвать такси'"):
            return self.is_visible(MainPageLocators.CALL_TAXI_BUTTON)

    def is_book_drive_button_active(self):
        with allure.step("Проверка активности кнопки 'Забронировать'"):
            return self.is_visible(MainPageLocators.BOOK_DRIVE_BUTTON)

    # Получение информации о маршруте
    def get_route_cost(self):
        with allure.step("Получение стоимости маршрута"):
            return self.get_text(MainPageLocators.ROUTE_COST)

    def get_route_time(self):
        with allure.step("Получение времени в пути"):
            return self.get_text(MainPageLocators.ROUTE_TIME)
    
    # Работа с тарифами такси
    def select_working_tariff(self):
        with allure.step("Выбор тарифа 'Рабочий'"):
            self.click(TaxiOrderLocators.WORKING_TARIFF)
    
    def get_all_tariffs(self):
        with allure.step("Получение всех тарифов"):
            return self.find_elements(TaxiOrderLocators.ALL_TARIFFS)
    
    def is_tariff_active(self):
        with allure.step("Проверка активности тарифа"):
            return self.is_visible(TaxiOrderLocators.ACTIVE_TARIFF)
    
    def get_active_tariff_price(self):
        with allure.step("Получение цены активного тарифа"):
            return self.get_text(TaxiOrderLocators.ACTIVE_TARIFF_PRICE)
    
    def hover_tariff_info(self, tariff_name):
        with allure.step(f"Наведение на иконку информации тарифа {tariff_name}"):
            tariff_locators = {
                "Рабочий": TaxiOrderLocators.WORKING_TARIFF,
                "Сонный": TaxiOrderLocators.SLEEPY_TARIFF,
                "Отпускной": TaxiOrderLocators.VACATION_TARIFF,
                "Разговорчивый": TaxiOrderLocators.TALKATIVE_TARIFF,
                "Утешительный": TaxiOrderLocators.COMFORTING_TARIFF,
                "Глянцевый": TaxiOrderLocators.GLOSSY_TARIFF
            }
            self.click(tariff_locators[tariff_name])
            
            self.hover(TaxiOrderLocators.ACTIVE_TARIFF_INFO_BUTTON)
    
    def is_tariff_modal_visible(self, tariff_name):
        with allure.step(f"Проверка видимости модального окна тарифа {tariff_name}"):
            modal_locators = {
                "Рабочий": TaxiOrderLocators.MODAL_INFO_WORKING,
                "Сонный": TaxiOrderLocators.MODAL_INFO_SLEEPY,
                "Отпускной": TaxiOrderLocators.MODAL_INFO_VACATION,
                "Разговорчивый": TaxiOrderLocators.MODAL_INFO_TALKATIVE,
                "Утешительный": TaxiOrderLocators.MODAL_INFO_COMFORTING,
                "Глянцевый": TaxiOrderLocators.MODAL_INFO_GLOSSY
            }
            return self.is_visible(modal_locators[tariff_name])
    
    def get_tariff_name_from_modal(self, tariff_name):
        with allure.step(f"Получение названия тарифа из модального окна: {tariff_name}"):
            name_locators = {
                "Рабочий": TaxiOrderLocators.NAME_WORKING,
                "Сонный": TaxiOrderLocators.NAME_SLEEPY,
                "Отпускной": TaxiOrderLocators.NAME_VACATION,
                "Разговорчивый": TaxiOrderLocators.NAME_TALKATIVE,
                "Утешительный": TaxiOrderLocators.NAME_COMFORTING,
                "Глянцевый": TaxiOrderLocators.NAME_GLOSSY
            }
            return self.get_text(name_locators[tariff_name])
    
    def get_tariff_description_from_modal(self, tariff_name):
        with allure.step(f"Получение описания тарифа '{tariff_name}' из модального окна"):
            description_locators = {
                "Рабочий": TaxiOrderLocators.DESCRIPTION_WORKING,
                "Сонный": TaxiOrderLocators.DESCRIPTION_SLEEPY,
                "Отпускной": TaxiOrderLocators.DESCRIPTION_VACATION,
                "Разговорчивый": TaxiOrderLocators.DESCRIPTION_TALKATIVE,
                "Утешительный": TaxiOrderLocators.DESCRIPTION_COMFORTING,
                "Глянцевый": TaxiOrderLocators.DESCRIPTION_GLOSSY
            }
            return self.get_text(description_locators[tariff_name])

    def click_requirements(self):
        with allure.step("Клик по блоку 'Требования к заказу'"):
            self.click(TaxiOrderLocators.FIELD_REQUIREMENTS)

    def click_laptop_slider(self):
        with allure.step("Клик по слайдеру 'Столик для ноутбука'"):
            self.click_requirements()
            self.click(TaxiOrderLocators.LAPTOP_SLIDER)
    
    def click_order_button(self):
        with allure.step("Клик по кнопке заказа"):
            self.click(TaxiOrderLocators.ORDER_BUTTON)
    
    # Работа с модальными окнами
    def is_order_modal_visible(self):
        with allure.step("Проверка видимости модального окна заказа"):
            return self.is_visible(ModalLocators.ORDER_MODAL_WINDOW)
    
    def get_order_header_title(self):
        with allure.step("Получение заголовка окна заказа"):
            return self.get_text(ModalLocators.ORDER_HEADER_TITLE)
    
    def get_order_header_time(self):
        with allure.step("Получение времени в заголовке окна заказа"):
            return self.get_text(ModalLocators.ORDER_HEADER_TIME)
    
    def is_timer_visible(self):
        with allure.step("Проверка видимости таймера"):
            return self.is_visible(ModalLocators.ORDER_HEADER_TIME)
    
    def click_details_button(self):
        with allure.step("Клик по кнопке 'Детали'"):
            self.click(ModalLocators.DETAILS_BUTTON)
    
    def click_cancel_button(self):
        with allure.step("Клик по кнопке 'Отмена'"):
            self.click(ModalLocators.CANCEL_BUTTON)
    
    def get_trip_price(self):
        with allure.step("Получение стоимости поездки"):
            return self.get_text(ModalLocators.TRIP_PRICE)
    
    def get_active_tariff_title(self):
        with allure.step("Получение названия активного тарифа"):
            return self.get_text(TaxiOrderLocators.ACTIVE_TARIFF_TITLE)
    
    def click_active_tariff_info(self):
        with allure.step("Клик на кнопку информации активного тарифа"):
            self.click(TaxiOrderLocators.ACTIVE_TARIFF_INFO_BUTTON)
    
    def get_hover_tariff_title(self):
        with allure.step("Получение названия тарифа при наведении"):
            return self.get_text(TaxiOrderLocators.HOVER_TARIFF_TITLE)
    
    def get_hover_tariff_description(self):
        with allure.step("Получение описания тарифа при наведении"):
            return self.get_text(TaxiOrderLocators.HOVER_TARIFF_DESCRIPTION)
    
    def get_working_tariff_price(self):
        with allure.step("Получение цены тарифа 'Рабочий'"):
            return self.get_text(TaxiOrderLocators.WORKING_TARIFF_PRICE)
    
    def get_phone_field_text(self):
        with allure.step("Получение текста поля телефона"):
            return self.get_text(TaxiOrderLocators.FIELD_PHONE)
    
    def get_payment_field_text(self):
        with allure.step("Получение текста поля способа оплаты"):
            return self.get_text(TaxiOrderLocators.FIELD_PAYMENT)
    
    def get_comment_field_text(self):
        with allure.step("Получение текста поля комментария"):
            try:
                self.click_requirements()
            except:
                pass
            
            placeholder_text = self.get_attribute(TaxiOrderLocators.FIELD_COMMENT, "placeholder")
            return placeholder_text if placeholder_text else self.get_text(TaxiOrderLocators.FIELD_COMMENT)
    
    def get_requirements_field_text(self):
        with allure.step("Получение текста поля требований"):
            return self.get_text(TaxiOrderLocators.FIELD_REQUIREMENTS)
