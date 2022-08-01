import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_homepage(self):
        driver = webdriver.Chrome()
        # driver.implicitly_wait(5)  -  First variant how to find element, not good
        # driver.find_element(By.CLASS_NAME, 'ui-input-search')
        wait = WebDriverWait(driver, 10, 0.2)  # Wait element 10 second and check every 0.2 seconds
        wait.until(ec.visibility_of_element_located(By.CLASS_NAME, 'ui-input-search'))



