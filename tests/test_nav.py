from os import error
from time import sleep
from selenium.webdriver.common.by import By

from tests.conftest import LOGIN_EMAIL, SIGNUP_EMAIL, SIGNUP_NAME, SIGNUP_PSWD
from tests.helper import login
from tests.locators import HEADER_KONSTR_LINK, HEADER_LK_LINK, HEADER_LOGO_LINK, HOME_LOGIN_BUTTON, HOME_ORDER_BUTTON, LK_EXIT_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, LOGIN_RECOVERY_BUTTON, LOGIN_SIGNUP_LINK, RECOVERY__LOGIN_BUTTON, SIGNUP_LOGIN_BUTTON, SIGNUP_NAME_INPUT, SIGNUP_PAROL_ERROR, SIGNUP_PAROL_INPUT, SIGNUP_SIGNUP_BUTTON

class TestNav:
    def test_lk_after_login(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()
        sleep(1)

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.education-services.ru/account/profile'
        

        driver.quit()

    def test_konstr_after_lk(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()

        button = driver.find_element(By.XPATH,HEADER_KONSTR_LINK)
        button.click()

        sleep(1)

        current_url = driver.current_url
        assert current_url.strip("/") == 'https://stellarburgers.education-services.ru'
        

        driver.quit()    

    def test_logo_after_lk(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()

        button = driver.find_element(By.XPATH,HEADER_LOGO_LINK)
        button.click()

        sleep(1)

        current_url = driver.current_url
        assert current_url.strip("/") == 'https://stellarburgers.education-services.ru'
        

        driver.quit()        

    def test_exit_after_lk(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()
        
        sleep(1)

        button = driver.find_element(By.XPATH,LK_EXIT_BUTTON)
        button.click()

        sleep(1)

        current_url = driver.current_url
        assert current_url.strip("/") == 'https://stellarburgers.education-services.ru/login'
        

        driver.quit()         
   