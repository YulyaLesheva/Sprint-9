import allure
import pytest
from data.test_data import TAXI_TARIFFS


@allure.feature("Тарифы такси")
class TestTaxiTariffs:
    
    @allure.title("Отображение формы заказа со всеми 6 тарифами")
    @allure.description("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_taxi_order_form_display(self, set_route):
        main_page = set_route
        
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        all_tariffs = main_page.get_all_tariffs()
        assert len(all_tariffs) == 6, f"Ожидалось 6 тарифов, найдено: {len(all_tariffs)}"
        
        assert main_page.is_tariff_active(), "Ни один тариф не активен"
        
        tariff_names = [tariff.text for tariff in all_tariffs]
        expected_names = [tariff["name"] for tariff in TAXI_TARIFFS.values()]
        
        for expected_name in expected_names:
            assert expected_name in tariff_names, f"Тариф '{expected_name}' не найден в списке"
    
    @allure.title("Отображение всплывающих окон с описанием тарифов")
    @allure.description("При наведении на иконку i отображается всплывающее окно с описанием тарифа")
    @pytest.mark.parametrize("tariff_name,tariff_data", [
        ("Рабочий", TAXI_TARIFFS["WORKING"]),
        ("Сонный", TAXI_TARIFFS["SLEEPY"]),
        ("Отпускной", TAXI_TARIFFS["VACATION"]),
        ("Разговорчивый", TAXI_TARIFFS["TALKATIVE"]),
        ("Утешительный", TAXI_TARIFFS["COMFORTING"]),
        ("Глянцевый", TAXI_TARIFFS["GLOSSY"])
    ])
    def test_tariff_tooltip_display(self, set_route, tariff_name, tariff_data):
        main_page = set_route
        
        if tariff_name in ["Сонный", "Разговорчивый"]:
            pytest.xfail("Баг с перепутанным описанием тарифов Сонный и Разговорчивый")
        
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        if tariff_name == "Рабочий":
            main_page.select_working_tariff()
        
        main_page.hover_tariff_info(tariff_name)

        assert main_page.is_tariff_modal_visible(tariff_name), f"Модальное окно тарифа '{tariff_name}' не отображается"
        
        modal_name = main_page.get_tariff_name_from_modal(tariff_name)
        modal_description = main_page.get_tariff_description_from_modal(tariff_name)
        
        assert modal_name == tariff_data["name"], f"Название не совпадает: ожидалось '{tariff_data['name']}', получено '{modal_name}'"
        assert modal_description == tariff_data["description"], f"Описание не совпадает: ожидалось '{tariff_data['description']}', получено '{modal_description}'"
    
    @allure.title("Отображение блока с полями под тарифами")
    @allure.description("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий, Требования")
    def test_order_form_fields_display(self, set_route):
        main_page = set_route
        
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        phone_field = main_page.get_phone_field_text()
        payment_field = main_page.get_payment_field_text()
        comment_field = main_page.get_comment_field_text()
        requirements_field = main_page.get_requirements_field_text()
        
        assert phone_field, "Поле 'Телефон' не отображается"
        assert payment_field, "Поле 'Способ оплаты' не отображается"
        assert comment_field, "Поле 'Комментарий водителю' не отображается"
        assert requirements_field, "Поле 'Требования к заказу' не отображается"
    
    @allure.title("Выбор тарифа 'Рабочий' и включение чекбокса 'Столик для ноутбука'")
    @allure.description("Выбираем тариф 'Рабочий', включаем чекбокс 'Столик для ноутбука'")
    def test_working_tariff_selection_with_laptop_table(self, set_route):
        """Проверка выбора тарифа 'Рабочий' и включения чекбокса"""
        main_page = set_route
        
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        main_page.select_working_tariff()
        
        assert main_page.is_tariff_active(), "Тариф 'Рабочий' не активен"
        
        active_tariff_name = main_page.get_active_tariff_title()
        assert active_tariff_name == "Рабочий", f"Ожидался тариф 'Рабочий', получен '{active_tariff_name}'"
        
        main_page.click_laptop_slider()
        
        tariff_price = main_page.get_working_tariff_price()
        assert tariff_price, "Цена тарифа 'Рабочий' не отображается"
