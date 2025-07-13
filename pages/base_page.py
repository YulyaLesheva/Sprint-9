import allure
from abc import abstractmethod
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    @abstractmethod
    def url(self): ...

    def open(self):
        with allure.step(f"Открыть страницу по URL: {self.url}"):
            self.driver.get(self.url)
            self.wait.until(EC.url_to_be(self.url))

    def is_opened(self):
        with allure.step(f"Проверить, что страница открыта по URL: {self.url}"):
            return self.wait.until(EC.url_to_be(self.url))

    def click(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в элемент: {locator}"):
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def is_visible(self, locator):
        with allure.step(f"Проверка, что элемент видим: {locator}"):
            try:
                self.wait.until(EC.visibility_of_element_located(locator))
                return True
            except:
                return False

    def is_hidden(self, locator, timeout=5):
        with allure.step(f"Проверка, что элемент скрыт: {locator}"):
            try:
                WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
                return True
            except:
                return False

    def wait_for_element_visible(self, locator):
        with allure.step(f"Ожидание видимости элемента: {locator}"):
            return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        with allure.step(f"Ожидание кликабельности элемента: {locator}"):
            return self.wait.until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        with allure.step(f"Получение текста элемента: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text

    def get_attribute(self, locator, attribute):
        with allure.step(f"Получение атрибута '{attribute}' элемента: {locator}"):
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.get_attribute(attribute)

    def hover(self, locator):
        with allure.step(f"Наведение курсора на элемент: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()

    def find_elements(self, locator):
        with allure.step(f"Поиск элементов: {locator}"):
            return self.driver.find_elements(*locator)

    def is_element_present(self, locator):
        with allure.step(f"Проверка наличия элемента: {locator}"):
            try:
                self.wait.until(EC.presence_of_element_located(locator))
                return True
            except:
                return False
