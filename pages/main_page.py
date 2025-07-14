import allure
from pages.base_page import BasePage
from data.locators import MainPageLocators


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
        with allure.step("Получение заблокированных типов передвижения"):
            return self.find_elements(MainPageLocators.TYPES_DISABLED)
    
    def is_drive_type_available(self):
        with allure.step("Проверка доступности типа 'Драйв'"):
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
        with allure.step("Проверка видимости блока маршрута"):
            return self.is_visible(MainPageLocators.ROUTE_BLOCK)

    def is_route_points_visible(self):
        with allure.step("Проверка видимости точек маршрута"):
            waypoint_first = self.is_visible(MainPageLocators.WAYPOINT_FIRST)
            waypoint_second = self.is_visible(MainPageLocators.WAYPOINT_SECOND) 
            return waypoint_first and waypoint_second

    def get_route_points_general(self):
        with allure.step("Получение общих точек маршрута"):
            return self.find_elements(MainPageLocators.ROUTE_POINTS_GENERAL)

    # Состояние кнопок
    def is_call_taxi_button_active(self):
        with allure.step("Проверка активности кнопки 'Вызвать такси'"):
            return self.is_element_present(MainPageLocators.CALL_TAXI_BUTTON)

    def is_book_drive_button_active(self):
        with allure.step("Проверка активности кнопки 'Забронировать'"):
            return self.is_element_present(MainPageLocators.BOOK_DRIVE_BUTTON)

    # Информация о маршруте
    def get_route_cost(self):
        with allure.step("Получение стоимости маршрута"):
            return self.get_text(MainPageLocators.ROUTE_COST)

    def get_route_time(self):
        with allure.step("Получение времени маршрута"):
            return self.get_text(MainPageLocators.ROUTE_TIME)
