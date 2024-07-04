import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver(request):
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(time_to_wait=10)
    driver.get('https://www.advantageonlineshopping.com/')
    yield driver
def wait_until():
    wait = WebDriverWait
    driver.quit()