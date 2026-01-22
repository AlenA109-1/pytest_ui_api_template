# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

## Шаги:
1. Склонировать проект `git clone` https://github.com/AlenA109-1/pytest_ui_api_template.git
2. Установить все зависимости
3. Запустить тесты `pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- ./configuration - провайдер настроек
- mytest_config.ini - настройка для тестов
- ./testdata - провайдер тестовых данных
- test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests