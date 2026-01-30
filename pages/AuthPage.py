from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure
from configuration.ConfigProvider import ConfigProvider

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        url = ConfigProvider().get("ui", "base_url")
        self.__url = url
        self.__driver = driver

    @allure.step("Открыть браузер на странице https://www.labirint.ru/")
    def go(self) -> None:
        """Открывает браузер"""
        self.__driver.get(self.__url)

    @allure.step("Открыть и заполнить форму авторизации по номеру телефона {phone}")
    def login_as(self, phone: str) -> None:
        """Открывает и заполняет форму авторизации"""
        self.__driver.find_element(
            By.CLASS_NAME, "b-header-b-personal-e-icon-m-profile").click()
        
        #дождется, что поле ввода будет видимо
        input_phone = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "formvalidate-error")))
        input_phone.send_keys(phone)
        # self.__driver.find_element(By.CLASS_NAME, "formvalidate-error").send_keys(phone)
        
        reg_button = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#g-recap-0-btn")))
        reg_button.click()
        # self.__driver.find_element(By.CSS_SELECTOR, "#g-recap-0-btn").click()

    @allure.step("Убедиться, что появилось поле ввода пин-кода")
    def is_pin_input_visible(self) -> bool:
        """Показывает видимо ли поле ввода пин-кода"""
        try:
            wait = WebDriverWait(self.__driver, 10)  # ожидает до 10 секунд
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="_ _ _ _"]')))
            return True
        except NoSuchElementException:
            return False
        
        
        
        
        