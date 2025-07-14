import allure
from data.test_data import ADDRESSES, TAXI_TARIFFS, MESSAGES


@allure.feature("Полный сценарий заказа такси")
class TestFullTaxiOrderFlow:
    
    @allure.title("Полный сценарий заказа такси от начала до конца")
    @allure.description("Проверка полного флоу: ввод адресов → выбор режима → выбор тарифа → заказ → ожидание → завершение")
    def test_complete_taxi_order_flow(self, main_page, taxi_order_page, modal_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        taxi_order_page.click_laptop_slider()
        taxi_order_page.click_order_button()
        
        assert modal_page.is_order_modal_visible(), "Модальное окно заказа не отображается"
        assert modal_page.get_order_header_title() == MESSAGES["SEARCH_MACHINE"], "Неверный заголовок заказа"
        
        modal_page.wait_for_custom_condition(
            lambda driver: "мин. и приедет" in modal_page.get_order_header_title() or 
                          "Поиск машины" in modal_page.get_order_header_title()
        )
        
        final_title = modal_page.get_order_header_title()
        assert "мин. и приедет" in final_title or "Поиск машины" in final_title, f"Неожиданный заголовок: {final_title}"
        
        modal_page.click_details_button()
        trip_price = modal_page.get_trip_price()
        assert trip_price, "Стоимость поездки не отображается"


@allure.feature("Тарифы такси")
class TestTaxiTariffs:
    
    @allure.title("Проверка тарифа 'Рабочий'")
    def test_working_tariff(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_working_tariff()
        taxi_order_page.hover_tariff_info("Рабочий")
        
        assert taxi_order_page.is_tariff_modal_visible("Рабочий")
        assert taxi_order_page.get_tariff_name_from_modal("Рабочий") == TAXI_TARIFFS["WORKING"]["name"]
        assert taxi_order_page.get_tariff_description_from_modal("Рабочий") == TAXI_TARIFFS["WORKING"]["description"]
    
    @allure.title("Проверка тарифа 'Сонный'")
    def test_sleepy_tariff(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_sleepy_tariff()
        taxi_order_page.hover_tariff_info("Сонный")
        
        assert taxi_order_page.is_tariff_modal_visible("Сонный")
        assert taxi_order_page.get_tariff_name_from_modal("Сонный") == TAXI_TARIFFS["SLEEPY"]["name"]
        assert taxi_order_page.get_tariff_description_from_modal("Сонный") == TAXI_TARIFFS["SLEEPY"]["description"]
    
    @allure.title("Проверка тарифа 'Отпускной'")
    def test_vacation_tariff(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_vacation_tariff()
        taxi_order_page.hover_tariff_info("Отпускной")
        
        assert taxi_order_page.is_tariff_modal_visible("Отпускной")
        assert taxi_order_page.get_tariff_name_from_modal("Отпускной") == TAXI_TARIFFS["VACATION"]["name"]
        assert taxi_order_page.get_tariff_description_from_modal("Отпускной") == TAXI_TARIFFS["VACATION"]["description"]
    
    @allure.title("Проверка тарифа 'Разговорчивый'")
    def test_talkative_tariff(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_talkative_tariff()
        taxi_order_page.hover_tariff_info("Разговорчивый")
        
        assert taxi_order_page.is_tariff_modal_visible("Разговорчивый")
        assert taxi_order_page.get_tariff_name_from_modal("Разговорчивый") == TAXI_TARIFFS["TALKATIVE"]["name"]
        assert taxi_order_page.get_tariff_description_from_modal("Разговорчивый") == TAXI_TARIFFS["TALKATIVE"]["description"]
    
    @allure.title("Проверка тарифа 'Утешительный'")
    def test_comforting_tariff(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_comforting_tariff()
        taxi_order_page.hover_tariff_info("Утешительный")
        
        assert taxi_order_page.is_tariff_modal_visible("Утешительный")
        assert taxi_order_page.get_tariff_name_from_modal("Утешительный") == TAXI_TARIFFS["COMFORTING"]["name"]
        assert taxi_order_page.get_tariff_description_from_modal("Утешительный") == TAXI_TARIFFS["COMFORTING"]["description"]
    
    @allure.title("Проверка тарифа 'Глянцевый'")
    def test_glossy_tariff(self, main_page, taxi_order_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        main_page.select_fast_route()
        main_page.click_call_taxi_button()
        
        taxi_order_page.select_glossy_tariff()
        taxi_order_page.hover_tariff_info("Глянцевый")
        
        assert taxi_order_page.is_tariff_modal_visible("Глянцевый")
        assert taxi_order_page.get_tariff_name_from_modal("Глянцевый") == TAXI_TARIFFS["GLOSSY"]["name"]
        assert taxi_order_page.get_tariff_description_from_modal("Глянцевый") == TAXI_TARIFFS["GLOSSY"]["description"]


@allure.feature("Маршруты")
class TestRoutes:
    
    @allure.title("Проверка всех режимов маршрута")
    def test_all_route_modes(self, main_page):
        main_page.set_addresses(ADDRESSES["ADDRESS_1"], ADDRESSES["ADDRESS_2"])
        
        main_page.select_optimal_route()
        assert main_page.is_route_mode_active()
        
        main_page.select_fast_route()
        assert main_page.is_route_mode_active()
        
        main_page.select_mine_route()
        assert main_page.is_route_mode_active()
