"""Тестовые данные и константы для проекта"""

# Предустановленные адреса из ТЗ
ADDRESSES = {
    "ADDRESS_1": "Хамовнический вал, 34",
    "ADDRESS_2": "Зубовский бульвар, 37"
}

# Описания тарифов такси
TAXI_TARIFFS = {
    "WORKING": {
        "name": "Рабочий",
        "description": "Для деловых особ, которых отвлекают"
    },
    "SLEEPY": {
        "name": "Сонный", 
        "description": "Если мысли не выходят из головы"
    },
    "VACATION": {
        "name": "Отпускной",
        "description": "Если пришла пора отдохнуть"
    },
    "TALKATIVE": {
        "name": "Разговорчивый",
        "description": "Для тех, кто не выспался"
    },
    "COMFORTING": {
        "name": "Утешительный",
        "description": "Если хочется свернуться калачиком"
    },
    "GLOSSY": {
        "name": "Глянцевый",
        "description": "Если нужно блистать"
    }
}

# Описания тарифов драйва
DRIVE_TARIFFS = {
    "EVERYDAY": {
        "name": "Повседневный",
        "car": "BMW 750",
        "description": "Просто по делам, ничего лишнего"
    },
    "HIKING": {
        "name": "Походный",
        "car": "KIA RIO", 
        "description": "Для путешествий"
    },
    "LUXURY": {
        "name": "Роскошный",
        "car": "PORSCHE 911",
        "description": "Блеск, мощь, глянец"
    }
}

# Текстовые сообщения для проверок
MESSAGES = {
    "SAME_ROUTE": "Авто Бесплатно В пути 0 мин.",
    "SEARCH_MACHINE": "Поиск машины",
    "MACHINE_BOOKED": "Машина забронирована",
    "FREE_WAITING": "Бесплатное ожидание"
}

# Тестовые данные для форм
TEST_DATA = {
    "PHONE": "+7 999 123 45 67",
    "PAYMENT_METHOD": "Наличные",
    "DRIVER_COMMENT": "Тестовый комментарий водителю",
    "ORDER_REQUIREMENTS": "Тестовые требования к заказу",
    "FIRST_NAME": "Тест",
    "LAST_NAME": "Тестов",
    "BIRTH_DATE": "01.01.1990",
    "LICENSE_NUMBER": "1234567890"
}
