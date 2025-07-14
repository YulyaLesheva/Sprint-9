import allure
from pages.base_page import BasePage
from data.locators import TaxiOrderLocators


class TaxiOrderPage(BasePage):
    url = "https://ez-route.stand.praktikum-services.ru/"

    def get_all_tariffs(self):
        with allure.step("Получение всех тарифов"):
            return self.find_elements(TaxiOrderLocators.ALL_TARIFFS)

    def is_tariff_active(self):
        with allure.step("Проверка активности тарифа"):
            return self.is_visible(TaxiOrderLocators.ACTIVE_TARIFF)

    def get_active_tariff_price(self):
        with allure.step("Получение цены активного тарифа"):
            return self.get_text(TaxiOrderLocators.ACTIVE_TARIFF_PRICE)

    def select_working_tariff(self):
        with allure.step("Выбор тарифа 'Рабочий'"):
            self.click(TaxiOrderLocators.WORKING_TARIFF)

    def select_sleepy_tariff(self):
        with allure.step("Выбор тарифа 'Сонный'"):
            self.click(TaxiOrderLocators.SLEEPY_TARIFF)

    def select_vacation_tariff(self):
        with allure.step("Выбор тарифа 'Отпускной'"):
            self.click(TaxiOrderLocators.VACATION_TARIFF)

    def select_talkative_tariff(self):
        with allure.step("Выбор тарифа 'Разговорчивый'"):
            self.click(TaxiOrderLocators.TALKATIVE_TARIFF)

    def select_comforting_tariff(self):
        with allure.step("Выбор тарифа 'Утешительный'"):
            self.click(TaxiOrderLocators.COMFORTING_TARIFF)

    def select_glossy_tariff(self):
        with allure.step("Выбор тарифа 'Глянцевый'"):
            self.click(TaxiOrderLocators.GLOSSY_TARIFF)

    def hover_tariff_info(self, tariff_name):
        tariff_info_locators = {
            "Рабочий": TaxiOrderLocators.INFO_WORKING,
            "Сонный": TaxiOrderLocators.INFO_SLEEPY,
            "Отпускной": TaxiOrderLocators.INFO_VACATION,
            "Разговорчивый": TaxiOrderLocators.INFO_TALKATIVE,
            "Утешительный": TaxiOrderLocators.INFO_COMFORTING,
            "Глянцевый": TaxiOrderLocators.INFO_GLOSSY
        }
        
        with allure.step(f"Наведение курсора на информацию о тарифе '{tariff_name}'"):
            locator = tariff_info_locators.get(tariff_name)
            if locator:
                self.hover(locator)

    def is_tariff_modal_visible(self, tariff_name):
        tariff_modal_locators = {
            "Рабочий": TaxiOrderLocators.MODAL_INFO_WORKING,
            "Сонный": TaxiOrderLocators.MODAL_INFO_SLEEPY,
            "Отпускной": TaxiOrderLocators.MODAL_INFO_VACATION,
            "Разговорчивый": TaxiOrderLocators.MODAL_INFO_TALKATIVE,
            "Утешительный": TaxiOrderLocators.MODAL_INFO_COMFORTING,
            "Глянцевый": TaxiOrderLocators.MODAL_INFO_GLOSSY
        }
        
        with allure.step(f"Проверка видимости модального окна тарифа '{tariff_name}'"):
            locator = tariff_modal_locators.get(tariff_name)
            if locator:
                return self.is_visible(locator)
            return False

    def get_tariff_name_from_modal(self, tariff_name):
        tariff_name_locators = {
            "Рабочий": TaxiOrderLocators.NAME_WORKING,
            "Сонный": TaxiOrderLocators.NAME_SLEEPY,
            "Отпускной": TaxiOrderLocators.NAME_VACATION,
            "Разговорчивый": TaxiOrderLocators.NAME_TALKATIVE,
            "Утешительный": TaxiOrderLocators.NAME_COMFORTING,
            "Глянцевый": TaxiOrderLocators.NAME_GLOSSY
        }
        
        with allure.step(f"Получение названия тарифа '{tariff_name}' из модального окна"):
            locator = tariff_name_locators.get(tariff_name)
            if locator:
                return self.get_text(locator)
            return ""

    def get_tariff_description_from_modal(self, tariff_name):
        tariff_description_locators = {
            "Рабочий": TaxiOrderLocators.DESCRIPTION_WORKING,
            "Сонный": TaxiOrderLocators.DESCRIPTION_SLEEPY,
            "Отпускной": TaxiOrderLocators.DESCRIPTION_VACATION,
            "Разговорчивый": TaxiOrderLocators.DESCRIPTION_TALKATIVE,
            "Утешительный": TaxiOrderLocators.DESCRIPTION_COMFORTING,
            "Глянцевый": TaxiOrderLocators.DESCRIPTION_GLOSSY
        }
        
        with allure.step(f"Получение описания тарифа '{tariff_name}' из модального окна"):
            locator = tariff_description_locators.get(tariff_name)
            if locator:
                return self.get_text(locator)
            return ""

    def click_requirements(self):
        with allure.step("Клик по требованиям"):
            self.click(TaxiOrderLocators.FIELD_REQUIREMENTS)

    def click_laptop_slider(self):
        with allure.step("Клик по слайдеру ноутбука"):
            self.click_requirements()
            self.click(TaxiOrderLocators.LAPTOP_SLIDER)

    def click_order_button(self):
        with allure.step("Клик по кнопке 'Заказать'"):
            self.click(TaxiOrderLocators.ORDER_BUTTON)

    def get_active_tariff_title(self):
        with allure.step("Получение названия активного тарифа"):
            return self.get_text(TaxiOrderLocators.ACTIVE_TARIFF_TITLE)

    def click_active_tariff_info(self):
        with allure.step("Клик по информации активного тарифа"):
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
        with allure.step("Получение текста поля оплаты"):
            return self.get_text(TaxiOrderLocators.FIELD_PAYMENT)

    def get_comment_field_text(self):
        with allure.step("Получение текста поля комментария"):
            return self.get_text(TaxiOrderLocators.FIELD_COMMENT)

    def get_requirements_field_text(self):
        with allure.step("Получение текста поля требований"):
            return self.get_text(TaxiOrderLocators.FIELD_REQUIREMENTS) 