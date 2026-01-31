from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure
from configuration.ConfigProvider import ConfigProvider

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        url = ConfigProvider().get("ui", "base_url")
        self.__url = url
        self.__driver = driver

    @allure.step("Открыть браузер на странице https://www.labirint.ru/")
    def go(self) -> None:
        """Открывает браузер"""
        self.__driver.get(self.__url)

    @allure.step("Ввести текст {namebook} в строку для поиска, нажать кнопку /""Искать/""")
    def search_book(self, namebook: str) -> None:
        """Вводит в строку для поиска, нажимает кнопку поиска"""
        search_input = WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.ID, "search-field")))
        search_input.clear()
        search_input.send_keys(namebook)
        self.__driver.find_element(By.CSS_SELECTOR, "span.b-header-b-search-e-btntxt").click()
        
    @allure.step("Нажать кнопку /""В корзину/"" на первой карточке товара")
    def add_book_to_cart(self):
        """Находит первую книгу, нажимает кнопку добавления в корзину"""
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.gtm-watched")))
        # Находим первую книгу/карточку товара
        first_book = self.__driver.find_element(By.CSS_SELECTOR, "div.gtm-watched:first-child")
        btn_to_cart = first_book.find_element(By.CSS_SELECTOR, "a.btn-tocart")
        btn_to_cart.click()

    @allure.step("Посмотреть значение счетчика товаров корзины")
    def get_cart_count(self) -> int:
        """Возвращает значение счетчика товаров корзины"""
        vcart = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.j-cart-count")))
        cart_count = int(vcart.text)
        return cart_count

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
               
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.j-cart-count"))).click()
        
        
    @allure.step("Отметить книгу отложенной")
    def put_into_favorites(self) -> None:
        """Добавляет первую книгу в Отложено"""
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-card")))
        first_book = self.__driver.find_element(By.CSS_SELECTOR, "div.product-card")
        fav_btn = first_book.find_element(By.CSS_SELECTOR, "a.btn-like")
        fav_btn.click()

    @allure.step("Перейти в Отложено")
    def go_to_favorites(self) -> None:
        """Переходит в раздел Отложено"""
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.b-header-b-personal-e-icon-m-putorder"))).click()
        
    @allure.step("Убедиться, что книга '{namebook}' есть в отложенных")
    def is_book_in_favorites(self, namebook) -> bool:
        """Проверяет, есть ли книга с указанным названием в отложенных"""
        try:
            fav_book = WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'product-title')]//a[contains(text(), '{namebook}')]")))
            return fav_book.is_displayed()
        except:
            return False
