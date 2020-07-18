import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', default="en", action='store', help="Choose language")


@pytest.fixture(scope="class")
def browser(request):
    browser = request.config.getoption("browser")
    if browser.lower() == "chrome":
        print("\nstart chrome browser for test..")
        language = request.config.getoption('language')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser.lower()== "firefox":
        print("\nstart firefox browser for test..")
        language = request.config.getoption('language')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
