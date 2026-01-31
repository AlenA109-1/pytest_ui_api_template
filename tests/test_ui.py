from pages.MainPage import MainPage
from pages.AuthPage import AuthPage
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_auth(browser, test_data: dict):  #тест работает раз 10, потом появляется капча
    phone = test_data.get("phone")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(phone)

    with allure.step("Проверить, что после заполнения формы авторизации появляется поле ввода пин-кода"):
        assert auth_page.is_pin_input_visible(), "Поле ввода пин-кода не появилось, проверьте введенные данные"


@pytest.mark.ui
def test_search_book(browser):
    """Поиск книги по названию"""  
    namebook = "огниво"
    main_page = MainPage(browser)
    main_page.go()
    main_page.search_book(namebook)

    result = WebDriverWait(browser, 10).until(lambda d: d.find_elements(By.CLASS_NAME, "product-card__link-mobile"))
      
    with allure.step("Убедиться, что найдена хотя бы одна книга - карточка товара"):
        assert len(result) > 0, "Не найдено ни одной книги или товара"
   
@pytest.mark.ui
def test_add_to_cart(browser):
    """Добавление в корзину"""
    main_page = MainPage(browser)
    main_page.go()
    main_page.search_book("энциклопедия")
    count_before = main_page.get_cart_count()
    main_page.add_book_to_cart()
    count_after = main_page.get_cart_count()

    with allure.step("Убедиться, что в корзине стало на 1 книгу больше"):
        assert count_after == count_before + 1, "Проверить вручную"

@pytest.mark.ui
def test_go_to_cart(browser):
    """Переход в корзину по иконке"""
    main_page = MainPage(browser)
    main_page.go()
    main_page.go_to_cart()
    
    with allure.step("Убедиться, что по клику на иконку корзины происходит переход на страницу корзины"):
        assert "/cart/" in browser.current_url, "Проверить вручную переход на страницу корзины"

@pytest.mark.ui
def test_add_book_to_favorites(browser):
    """Добавление книги в Отложено"""
    main_page = MainPage(browser)
    namebook = "Волкодав"  
    main_page.go()
    main_page.search_book(namebook)
    main_page.put_into_favorites()
    main_page.go_to_favorites()
    resp = main_page.is_book_in_favorites(namebook)

    with allure.step("Убедиться, что по клику на иконку Избранное происходит переход на страницу Отложено"):
        assert "/putorder/" in browser.current_url, "Проверить вручную переход на страницу Отложено"

    with allure.step("Убедиться, что книга добавлена в Отложено"):
        assert resp == True, f'Книга "{namebook}" не найдена в отложенных'
 
    
