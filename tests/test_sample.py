import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.implicitly_wait_value(10)
def test_sample_web(driver):
    element = driver.find_element(by=By.ID, value="menuUserLink")
    element.click()

    pop_up = driver.find_element(by=By.CSS_SELECTOR, value=".PopUp")
    assert pop_up.is_displayed()
    sign_in_btn = driver.find_element(value='sign_in_btn')
    assert not sign_in_btn.is_enabled()

    username_input = driver.find_element(by=By.NAME, value='username')
    username_input.clear()
    username_input.send_keys('Dod')

    password_input = driver.find_element(by=By.XPATH, value="//div[@class='inputContainer ng-scope']/child::input["
                                                            "@type='password']")
    password_input.clear()
    password_input.send_keys('Bk1153824')

    assert sign_in_btn.is_enabled()
    sign_in_btn.click()
    driver.quit()
