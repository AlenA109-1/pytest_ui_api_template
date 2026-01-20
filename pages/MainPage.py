from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.labirint.ru/"
        self.__driver = driver

    # def search_by_namebook(self):

    # def search_by_author(self):

    # def search_null(self):

    