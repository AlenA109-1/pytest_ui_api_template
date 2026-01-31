import pytest
import allure
from selenium import webdriver

from api.SearchApi import SearchApi
from configuration.ConfigProvider import ConfigProvider
from configuration.DataProvider import DataProvider

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        timeout_iw = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")

        if browser_name == 'chrome':
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
      
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> SearchApi:
    # return SearchApi("https://www.labirint.ru/")
    return SearchApi(ConfigProvider().get("ui", "base_url"))

@pytest.fixture
def test_data():
    dt_provider = DataProvider()
    return dt_provider