# Fixtures - decorators for functions
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need browser UI
    options.add_argument('--start-maximized')  # Start browser on fullscreen mode
    options.add_argument('--windows-size=1280,720')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)  # If driver not in python folder use executable_path='C:/Users/...'
    return driver


@pytest.fixture(scope='function')  # functions means - every test will run in 'clean' browser. Session means - all test will runs in one session
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.dns-shop.ru'
    if request.cls is not None:  # If test in class then use driver with test class
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
