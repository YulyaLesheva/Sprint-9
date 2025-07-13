import allure


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:
    
    @allure.title("Отрисовка маршрута при вводе двух разных адресов")
    @allure.description("При вводе двух разных предустановленных адресов на карте отображаются две точки")
    def test_route_points_display_different_addresses(self, set_route):
        main_page = set_route
        
        assert main_page.is_route_points_visible(), "Точки маршрута не отображаются на карте"
        
        route_points = main_page.get_route_points_general()
        assert len(route_points) >= 2, f"Ожидалось минимум 2 точки маршрута, найдено: {len(route_points)}"
    
    @allure.title("Отрисовка блока выбора маршрута при вводе двух разных адресов")
    @allure.description("При вводе двух разных адресов под выбором адресов отображается блок с выбором маршрута")
    def test_route_block_display_different_addresses(self, set_route):
        main_page = set_route
        
        assert main_page.is_route_block_visible(), "Блок выбора маршрута не отображается"
        
        assert main_page.is_route_block_shown(), "Блок выбора маршрута не в состоянии 'shown'"
    
    @allure.title("Отрисовка блока выбора маршрута при вводе одинакового адреса")
    @allure.description("При вводе одинакового адреса отображается блок с текстом 'Авто Бесплатно В пути 0 мин.'")
    def test_route_block_display_same_addresses(self, set_same_route):
        main_page = set_same_route
        
        assert main_page.is_route_block_visible(), "Блок выбора маршрута не отображается"
        
        route_cost = main_page.get_route_cost()
        route_time = main_page.get_route_time()
        
        assert "Бесплатно" in route_cost, f"Ожидался текст 'Бесплатно', получен: {route_cost}"
        assert "0 мин" in route_time, f"Ожидался текст '0 мин', получен: {route_time}"
