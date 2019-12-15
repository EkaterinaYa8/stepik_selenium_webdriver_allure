from selenium import webdriver
import pytest
from datetime import datetime


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    browser = None
    if browser_name == 'Chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif browser_name == 'Firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')
    yield browser

    browser.quit()


@pytest.fixture
def languages_initial():
    languages_initial = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt',
                         'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']
    return languages_initial


@pytest.fixture
def link(request, languages_initial):
    link = 'http://selenium1py.pythonanywhere.com/{}/'.format(request.config.getoption("--language"))

    language_from_link = request.config.getoption("--language")
    if language_from_link == 'zh-cn':
        return link
    elif language_from_link == 'zh-hans':
        return 'http://selenium1py.pythonanywhere.com/zh-cn/'
    elif language_from_link == 'en':
        return 'http://selenium1py.pythonanywhere.com/en-gb/'
    else:
        assert language_from_link in languages_initial, 'Переданное значение языка в аргументах командной строки ' \
                                                        '--language={} ' \
                                                        'некорректно.\nДолжно быть использовано значение из ' \
                                                        'следующего списка:\n{} или \"en\", \"zh-cn\".' \
                                                        ''.format(request.config.getoption("--language"),
                                                                  languages_initial)
        return link


@pytest.fixture
def current_language(request):
    current_language = request.config.getoption('--language')
    return current_language


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome',
                     help='Выберите браузер: Chrome или Firefox.')
    parser.addoption('--language', action='store', default='en',
                     help='Выбрать язык для загрузки сайта из списка значений:\n'
                          '["ar", "ca", "cs", "da", "de", "en", "en-gb", "el", "es", "fi", "fr", "it", '
                          '"ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-cn", "zh-hans"]\n, '
                          'где "en" или "en-gb" используется для выбора английского языка; \n'
                          '"zh-cn" или "zh-hans" используется для выбора китайского языка.')
