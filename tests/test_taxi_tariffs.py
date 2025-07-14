import allure
from data.test_data import ADDRESSES, TAXI_TARIFFS


@allure.feature("Тарифы такси")
class TestTaxiTariffs:
    
    @allure.title("Отображение формы заказа со всеми 6 тарифами")
    @allure.description("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_taxi_order_form_display(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        all_tariffs = taxi_order_page.get_all_tariffs()
        assert len(all_tariffs) == 6, f"Ожидалось 6 тарифов, найдено: {len(all_tariffs)}"
        assert taxi_order_page.is_tariff_active(), "Ни один тариф не активен"
        
        tariff_names = [tariff.text for tariff in all_tariffs]
        expected_names = [tariff["name"] for tariff in TAXI_TARIFFS.values()]
        
        for expected_name in expected_names:
            assert expected_name in tariff_names, f"Тариф '{expected_name}' не найден в списке"
    
    @allure.title("Проверка тарифа 'Рабочий'")
    @allure.description("Проверка отображения всплывающего окна с описанием тарифа 'Рабочий'")
    def test_working_tariff_tooltip(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        taxi_order_page.hover_tariff_info("Рабочий")
        
        assert taxi_order_page.is_tariff_modal_visible("Рабочий"), "Модальное окно тарифа 'Рабочий' не отображается"
        
        modal_name = taxi_order_page.get_tariff_name_from_modal("Рабочий")
        modal_description = taxi_order_page.get_tariff_description_from_modal("Рабочий")
        
        assert modal_name == TAXI_TARIFFS["WORKING"]["name"]
        assert modal_description == TAXI_TARIFFS["WORKING"]["description"]
    
    @allure.title("Проверка тарифа 'Сонный'")
    @allure.description("Проверка отображения всплывающего окна с описанием тарифа 'Сонный'")
    def test_sleepy_tariff_tooltip(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_sleepy_tariff()
        taxi_order_page.hover_tariff_info("Сонный")
        
        assert taxi_order_page.is_tariff_modal_visible("Сонный"), "Модальное окно тарифа 'Сонный' не отображается"
        
        modal_name = taxi_order_page.get_tariff_name_from_modal("Сонный")
        modal_description = taxi_order_page.get_tariff_description_from_modal("Сонный")
        
        assert modal_name == TAXI_TARIFFS["SLEEPY"]["name"]
        assert modal_description == TAXI_TARIFFS["SLEEPY"]["description"]
    
    @allure.title("Проверка тарифа 'Отпускной'")
    @allure.description("Проверка отображения всплывающего окна с описанием тарифа 'Отпускной'")
    def test_vacation_tariff_tooltip(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_vacation_tariff()
        taxi_order_page.hover_tariff_info("Отпускной")
        
        assert taxi_order_page.is_tariff_modal_visible("Отпускной"), "Модальное окно тарифа 'Отпускной' не отображается"
        
        modal_name = taxi_order_page.get_tariff_name_from_modal("Отпускной")
        modal_description = taxi_order_page.get_tariff_description_from_modal("Отпускной")
        
        assert modal_name == TAXI_TARIFFS["VACATION"]["name"]
        assert modal_description == TAXI_TARIFFS["VACATION"]["description"]
    
    @allure.title("Проверка тарифа 'Разговорчивый'")
    @allure.description("Проверка отображения всплывающего окна с описанием тарифа 'Разговорчивый'")
    def test_talkative_tariff_tooltip(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_talkative_tariff()
        taxi_order_page.hover_tariff_info("Разговорчивый")
        
        assert taxi_order_page.is_tariff_modal_visible("Разговорчивый"), "Модальное окно тарифа 'Разговорчивый' не отображается"
        
        modal_name = taxi_order_page.get_tariff_name_from_modal("Разговорчивый")
        modal_description = taxi_order_page.get_tariff_description_from_modal("Разговорчивый")
        
        assert modal_name == TAXI_TARIFFS["TALKATIVE"]["name"]
        assert modal_description == TAXI_TARIFFS["TALKATIVE"]["description"]
    
    @allure.title("Проверка тарифа 'Утешительный'")
    @allure.description("Проверка отображения всплывающего окна с описанием тарифа 'Утешительный'")
    def test_comforting_tariff_tooltip(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_comforting_tariff()
        taxi_order_page.hover_tariff_info("Утешительный")
        
        assert taxi_order_page.is_tariff_modal_visible("Утешительный"), "Модальное окно тарифа 'Утешительный' не отображается"
        
        modal_name = taxi_order_page.get_tariff_name_from_modal("Утешительный")
        modal_description = taxi_order_page.get_tariff_description_from_modal("Утешительный")
        
        assert modal_name == TAXI_TARIFFS["COMFORTING"]["name"]
        assert modal_description == TAXI_TARIFFS["COMFORTING"]["description"]
    
    @allure.title("Проверка тарифа 'Глянцевый'")
    @allure.description("Проверка отображения всплывающего окна с описанием тарифа 'Глянцевый'")
    def test_glossy_tariff_tooltip(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_glossy_tariff()
        taxi_order_page.hover_tariff_info("Глянцевый")
        
        assert taxi_order_page.is_tariff_modal_visible("Глянцевый"), "Модальное окно тарифа 'Глянцевый' не отображается"
        
        modal_name = taxi_order_page.get_tariff_name_from_modal("Глянцевый")
        modal_description = taxi_order_page.get_tariff_description_from_modal("Глянцевый")
        
        assert modal_name == TAXI_TARIFFS["GLOSSY"]["name"]
        assert modal_description == TAXI_TARIFFS["GLOSSY"]["description"]
    
    @allure.title("Отображение блока с полями под тарифами")
    @allure.description("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий, Требования")
    def test_order_form_fields_display(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        phone_field = taxi_order_page.get_phone_field_text()
        payment_field = taxi_order_page.get_payment_field_text()
        comment_field = taxi_order_page.get_comment_field_text()
        requirements_field = taxi_order_page.get_requirements_field_text()
        
        assert phone_field, "Поле 'Телефон' не отображается"
        assert payment_field, "Поле 'Способ оплаты' не отображается"
        assert comment_field, "Поле 'Комментарий водителю' не отображается"
        assert requirements_field, "Поле 'Требования к заказу' не отображается"
    
    @allure.title("Выбор тарифа 'Рабочий' и включение чекбокса 'Столик для ноутбука'")
    @allure.description("Выбираем тариф 'Рабочий', включаем чекбокс 'Столик для ноутбука'")
    def test_working_tariff_selection_with_laptop_table(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        
        assert taxi_order_page.is_tariff_active(), "Тариф 'Рабочий' не активен"
        
        active_tariff_name = taxi_order_page.get_active_tariff_title()
        assert active_tariff_name == "Рабочий", f"Ожидался тариф 'Рабочий', получен '{active_tariff_name}'"
        
        taxi_order_page.click_laptop_slider()
        
        tariff_price = taxi_order_page.get_working_tariff_price()
        assert tariff_price, "Цена тарифа 'Рабочий' не отображается"
