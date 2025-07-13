import allure


@allure.feature("Переключение видов маршрута")
class TestRouteSwitching:
    
    @allure.title("Переключение между видами маршрута с пересчетом времени и стоимости")
    @allure.description("При переключении между Оптимальный/Быстрый происходит пересчет времени и стоимости")
    def test_route_mode_switching_recalculation(self, set_route):
        main_page = set_route
        
        main_page.select_optimal_route()
        
        assert main_page.is_route_mode_active(), "Режим маршрута не активен после переключения"
        
        optimal_cost = main_page.get_route_cost()
        optimal_time = main_page.get_route_time()
        
        main_page.select_fast_route()
        
        fast_cost = main_page.get_route_cost()
        fast_time = main_page.get_route_time()
        
        assert optimal_cost != fast_cost or optimal_time != fast_time, \
            f"Пересчет не произошел: оптимальный ({optimal_cost}, {optimal_time}) == быстрый ({fast_cost}, {fast_time})"
    
    @allure.title("Переключение на режим 'Свой' активирует типы передвижения")
    @allure.description("При переключении на вид маршрута 'Свой' становятся активны типы передвижения")
    def test_custom_route_activates_transport_types(self, set_route):
        main_page = set_route
        
        main_page.select_mine_route()
        
        assert main_page.is_route_mode_active(), "Режим 'Свой' не активен"
        
        assert main_page.is_types_container_visible(), "Контейнер типов передвижения не отображается"
        
        active_types = main_page.get_active_types()
        assert len(active_types) > 0, "Нет активных типов передвижения в режиме 'Свой'"
        
        disabled_types = main_page.get_disabled_types()
        assert len(disabled_types) == 0, f"Обнаружены неактивные типы передвижения: {len(disabled_types)}"
    
    @allure.title("Активность кнопки 'Вызвать такси' в режиме 'Быстрый'")
    @allure.description("При выборе вида маршрута 'Быстрый' активна кнопка 'Вызвать такси'")
    def test_call_taxi_button_active_in_fast_mode(self, set_route):
        main_page = set_route
        
        main_page.select_fast_route()
        
        assert main_page.is_call_taxi_button_active(), "Кнопка 'Вызвать такси' не активна в режиме 'Быстрый'"
    
    @allure.title("Активность кнопки 'Забронировать' при выборе типа 'Драйв'")
    @allure.description("При выборе вида маршрута 'Свой', типа передвижения 'Драйв' активна кнопка 'Забронировать'")
    def test_book_drive_button_active_in_drive_mode(self, set_route):
        main_page = set_route
        
        main_page.select_mine_route()
        
        assert main_page.is_drive_type_available(), "Тип передвижения 'Драйв' не доступен"
        
        main_page.select_drive_type()
        
        assert main_page.is_book_drive_button_active(), "Кнопка 'Забронировать' не активна при выборе типа 'Драйв'"
