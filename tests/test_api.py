from api.SearchApi import SearchApi
import allure
import pytest

@pytest.mark.api
@pytest.mark.parametrize(
  "search_params, expected_text", [
    (("огниво",), "Андерсен"),                      # поиск на кириллице    
    (("20000",), "Верн"),                           # поиск по цифрам               
    (("The hound of the Baskervilles",), "Doyle"),  # поиск на латинице   
    (("ГРОЗА",), "Островский")                      # поиск по заглавным буквам
    ])

def test_search_by_bookname_positive(api_client: SearchApi, search_params: tuple, expected_text: str) -> None:
    search_query = search_params[0]  # извлекаем название книги из кортежа
    response = api_client.get('search/', params={'title': search_query})
          
    with allure.step("Убедиться, что запрос выполнен успешно - ожидаемый код ответа сервера 200"):
        assert response.status_code == 200, response.status_code
    
    with allure.step("Проверить, что в ответе содержится ожидаемое значение - фамилия автора"):
        assert expected_text in response.text, "Не найден ожидаемый ответ, убедиться вручную"

@pytest.mark.api
@pytest.mark.parametrize(
    "search_params, expected_text", [
    (("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",), "Все, что мы нашли в Лабиринте по запросу"),                      #поиск длинного текста        
    (("лит%0Aература",), "Все, что мы нашли в Лабиринте по запросу"),                           #поиск с управляющими символами               
    (("7в156!про.ю",), "Все, что мы нашли в Лабиринте по запросу"),                             #поиск по произвольному набору символов
    ])
def test_search_by_bookname_negative(api_client: SearchApi, search_params: tuple, expected_text: str) -> None:
    search_query = search_params[0]  # извлекаем название книги из кортежа
    response = api_client.get('search/', params={'title': search_query})
    
    with allure.step("Убедиться, что запрос выполнен успешно - ожидаемый код ответа сервера 200"):
        assert response.status_code == 200
    
    with allure.step("Проверить, что в ответе содержится стандартное сообщение"):
        assert expected_text in response.text

@pytest.mark.api
@pytest.mark.parametrize("search_params", [("hobbit",)])
def test_search_with_delete_negative(api_client: SearchApi, search_params: str) -> None:
    search_query = search_params[0]
    response = api_client.delete('search/', params={'title': search_query})
    
    with allure.step("Убедиться, что некорректный запрос не ломает всю систему - ожидаемый код ответа сервера 200"):
        assert response.status_code == 200

@pytest.mark.api
@pytest.mark.parametrize("search_params", [("",)])    
def test_empty_search(api_client: SearchApi, search_params: str) -> None:
    search_query = search_params[0]
    response = api_client.get('search/', params={'title': search_query})
    
    with allure.step("Убедиться, что пустой поиск не ломает всю систему - ожидаемый код ответа сервера 200"):
        assert response.status_code == 200

@pytest.mark.api
def test_go_to_cart(api_client: SearchApi) -> None:
    response = api_client.get('cart/')
    
    with allure.step("Убедиться, что запрос отрабатывает - ожидаемый код ответа сервера 200"):
        assert response.status_code == 200

    with allure.step("Убедиться, что произошел переход на страницу корзины"):
        assert '<span class="cart-title">Корзина</span>' in response.text



  
