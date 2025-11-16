from os import error
from time import sleep
from selenium.webdriver.common.by import By

from tests.conftest import LOGIN_EMAIL, SIGNUP_EMAIL, SIGNUP_NAME, SIGNUP_PSWD
from tests.locators import HEADER_LK_LINK, HOME_LOGIN_BUTTON, HOME_ORDER_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, LOGIN_RECOVERY_BUTTON, LOGIN_SIGNUP_LINK, RECOVERY__LOGIN_BUTTON, SIGNUP_LOGIN_BUTTON, SIGNUP_NAME_INPUT, SIGNUP_PAROL_ERROR, SIGNUP_PAROL_INPUT, SIGNUP_SIGNUP_BUTTON

class TestKonstruktor:
    def test_konstruktor_from_lk(self, driver):
        driver.get('https://stellarburgers.education-services.ru/') 
        
        button = driver.find_element(By.XPATH, HOME_LOGIN_BUTTON)
        button.click()

        email = driver.find_element(By.XPATH, LOGIN_EMAIL_INPUT)
        email.send_keys(LOGIN_EMAIL) 

        pswd = driver.find_element(By.XPATH, SIGNUP_PAROL_INPUT)
        pswd.send_keys(SIGNUP_PSWD) 
        
        button = driver.find_element(By.XPATH,LOGIN_LOGIN_BUTTON)
        button.click()

        sleep(1)

        button = driver.find_element(By.XPATH,HOME_ORDER_BUTTON)

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.education-services.ru/'
        

        driver.quit()

    def test_login_recovery(self, driver):
        driver.get('https://stellarburgers.education-services.ru/') 
        
        button = driver.find_element(By.XPATH, HOME_LOGIN_BUTTON)
        button.click()

        button = driver.find_element(By.XPATH, LOGIN_RECOVERY_BUTTON)
        button.click()

        button = driver.find_element(By.XPATH, RECOVERY__LOGIN_BUTTON)
        button.click()


        email = driver.find_element(By.XPATH, LOGIN_EMAIL_INPUT)
        email.send_keys(LOGIN_EMAIL) 

        pswd = driver.find_element(By.XPATH, SIGNUP_PAROL_INPUT)
        pswd.send_keys(SIGNUP_PSWD) 
        
        button = driver.find_element(By.XPATH,LOGIN_LOGIN_BUTTON)
        button.click()

        sleep(1)

        button = driver.find_element(By.XPATH,HOME_ORDER_BUTTON)

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.education-services.ru/'
        

        driver.quit()