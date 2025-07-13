from selenium.webdriver.common.by import By


class MainPageLocators:
    # Блок ввода адресов
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    
    # Точки маршрута на карте
    WAYPOINT_FIRST = (By.XPATH, '//ymaps[text()="улица Хамовнический Вал, 34"]')
    WAYPOINT_SECOND = (By.XPATH, '//ymaps[text()="Зубовский бульвар, 37"]')
    
    # Блок с выбором маршрута
    ROUTE_BLOCK = (By.CLASS_NAME, "type-picker")
    
    # Виды маршрута
    OPTIMAL_ROUTE = (By.XPATH, '//div[contains(text(), "Оптимальный")]')
    FAST_ROUTE = (By.XPATH, '//div[contains(text(), "Быстрый")]')
    MINE_ROUTE = (By.XPATH, '//div[contains(text(), "Свой")]')
    ACTIVE_MODE = (By.XPATH, '//div[contains(@class, "mode active")]')
    ROUTE_BLOCK_SHOWN = (By.XPATH, '//div[contains(@class, "type-picker shown")]')
    
    # Типы передвижения
    TYPES_CONTAINER = (By.XPATH, '//div[contains(@class, "types-container")]')
    TYPES_ACTIVE = (By.XPATH, '//div[contains(@class, "types-container")]/div[contains(@class, "type")]')
    TYPES_DISABLED = (By.XPATH, '//div[contains(@class, "types-container")]/div[contains(@class, "type") and contains(@class, "disabled")]')
    DRIVE_TYPE = (By.XPATH, '//div[contains(@class, "type drive")]')
    
    # Кнопки действий
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Вызвать такси")]')
    BOOK_DRIVE_BUTTON = (By.XPATH, '//button[contains(text(), "Забронировать")]')
    
    # Информация о маршруте
    ROUTE_COST = (By.CLASS_NAME, "text")
    ROUTE_TIME = (By.CLASS_NAME, "duration")
    
    # Точки маршрута (альтернативный локатор)
    ROUTE_POINTS_GENERAL = (By.XPATH, '//ymaps[contains(@id, "id_")]/ymaps')


class TaxiOrderLocators:
    # Тарифы такси
    ALL_TARIFFS = (By.XPATH, '//div[@class="tcard-title"]')
    ACTIVE_TARIFF = (By.XPATH, '//div[@class="tcard active"]')
    ACTIVE_TARIFF_PRICE = (By.XPATH, '//div[@class="tcard active"]/div[@class="tcard-price"]')
    
    WORKING_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Рабочий"]')
    SLEEPY_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Сонный"]')
    VACATION_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Отпускной"]')
    TALKATIVE_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Разговорчивый"]')
    COMFORTING_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Утешительный"]')
    GLOSSY_TARIFF = (By.XPATH, '//div[@class="tcard-title" and text()="Глянцевый"]')
    
    # Информационные иконки тарифов
    INFO_WORKING = (By.XPATH, '//div[@class="tcard active"]/button[@data-for="tariff-card-0"]')
    INFO_SLEEPY = (By.XPATH, '//div[@class="tcard active"]/button[@data-for="tariff-card-1"]')
    INFO_VACATION = (By.XPATH, '//div[@class="tcard active"]/button[@data-for="tariff-card-2"]')
    INFO_TALKATIVE = (By.XPATH, '//div[@class="tcard active"]/button[@data-for="tariff-card-3"]')
    INFO_COMFORTING = (By.XPATH, '//div[@class="tcard active"]/button[@data-for="tariff-card-4"]')
    INFO_GLOSSY = (By.XPATH, '//div[@class="tcard active"]/button[@data-for="tariff-card-5"]')
    
    # Модальные окна с информацией о тарифах
    MODAL_INFO_WORKING = (By.XPATH, '//*[@id="tariff-card-0" and contains(@class, "show")]')
    MODAL_INFO_SLEEPY = (By.XPATH, '//*[@id="tariff-card-1" and contains(@class, "show")]')
    MODAL_INFO_VACATION = (By.XPATH, '//*[@id="tariff-card-2" and contains(@class, "show")]')
    MODAL_INFO_TALKATIVE = (By.XPATH, '//*[@id="tariff-card-3" and contains(@class, "show")]')
    MODAL_INFO_COMFORTING = (By.XPATH, '//*[@id="tariff-card-4" and contains(@class, "show")]')
    MODAL_INFO_GLOSSY = (By.XPATH, '//*[@id="tariff-card-5" and contains(@class, "show")]')
    
    # Названия и описания в модальных окнах
    NAME_WORKING = (By.XPATH, '//div[@class="i-title" and text()="Рабочий"]')
    NAME_SLEEPY = (By.XPATH, '//div[@class="i-title" and text()="Сонный"]')
    NAME_VACATION = (By.XPATH, '//div[@class="i-title" and text()="Отпускной"]')
    NAME_TALKATIVE = (By.XPATH, '//div[@class="i-title" and text()="Разговорчивый"]')
    NAME_COMFORTING = (By.XPATH, '//div[@class="i-title" and text()="Утешительный"]')
    NAME_GLOSSY = (By.XPATH, '//div[@class="i-title" and text()="Глянцевый"]')
    
    DESCRIPTION_WORKING = (By.XPATH, '//div[@class="i-dPrefix" and text()="Для деловых особ, которых отвлекают"]')
    DESCRIPTION_SLEEPY = (By.XPATH, '//div[@class="i-dPrefix" and text()="Для тех, кто не выспался"]')
    DESCRIPTION_VACATION = (By.XPATH, '//div[@class="i-dPrefix" and text()="Если пришла пора отдохнуть"]')
    DESCRIPTION_TALKATIVE = (By.XPATH, '//div[@class="i-dPrefix" and text()="Если мысли не выходят из головы"]')
    DESCRIPTION_COMFORTING = (By.XPATH, '//div[@class="i-dPrefix" and text()="Если хочется свернуться калачиком"]')
    DESCRIPTION_GLOSSY = (By.XPATH, '//div[@class="i-dPrefix" and text()="Если нужно блистать"]')
    
    # Поля формы заказа
    FIELD_PHONE = (By.CLASS_NAME, "np-text")
    FIELD_PAYMENT = (By.CLASS_NAME, "pp-text")
    FIELD_COMMENT = (By.ID, "comment")
    FIELD_REQUIREMENTS = (By.CLASS_NAME, "reqs-head")
    
    # Элементы управления
    LAPTOP_SLIDER = (By.XPATH, '//span[contains(@class, "slider round")]')
    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    
    # Дополнительные локаторы
    ACTIVE_TARIFF_TITLE = (By.XPATH, '//div[contains(@class, "tcard active")]/div[contains(@class, "tcard-title")]')
    ACTIVE_TARIFF_INFO_BUTTON = (By.XPATH, '//div[contains(@class, "tcard active")]/button')
    HOVER_TARIFF_TITLE = (By.XPATH, '//div[contains(@class, "show border")]/div[@class="i-floating"]/div[@class="i-title"]')
    HOVER_TARIFF_DESCRIPTION = (By.XPATH, '//div[contains(@class, "show border")]/div[@class="i-floating"]/div[@class="i-dPrefix"]')
    WORKING_TARIFF_PRICE = (By.XPATH, '//div[contains(text(), "Рабочий")]/following-sibling::div')


# Примечание: Локаторы для DriveOrder не найдены в grabbed_locators.py
# Добавим их по мере необходимости после исследования интерфейса драйва


class ModalLocators:
    # Общие модальные окна
    ORDER_MODAL_WINDOW = (By.CLASS_NAME, "order-body")
    ORDER_HEADER_TITLE = (By.CLASS_NAME, "order-header-title")
    ORDER_HEADER_TIME = (By.CLASS_NAME, "order-header-time")
    CANCEL_BUTTON = (By.XPATH, '//div[contains(text(), "Отменить")]/preceding-sibling::button')
    DETAILS_BUTTON = (By.XPATH, '//div[contains(text(), "Детали")]/preceding-sibling::button')
    
    # Окно совершенного заказа такси
    CAR_NUMBER = (By.CLASS_NAME, "number")
    CAR_IMAGE = (By.XPATH, '//img[contains(@alt, "Car")]')
    DRIVER_IMAGE = (By.XPATH, '//img[contains(@src, "bender")]')
    DRIVER_RATING = (By.CLASS_NAME, "order-btn-rating")
    DRIVER_NAME = (By.XPATH, '//div[contains(@style, "cursor")]')
    TRIP_PRICE = (By.XPATH, '//div[contains(text(), "Стоимость - ")]')
