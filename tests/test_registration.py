from os import error
from time import sleep
from selenium.webdriver.common.by import By

from tests.conftest import SIGNUP_EMAIL, SIGNUP_NAME, SIGNUP_PSWD
from tests.locators import HOME_LOGIN_BUTTON, LOGIN_SIGNUP_LINK, SIGNUP_NAME_INPUT, SIGNUP_PAROL_ERROR, SIGNUP_PAROL_INPUT, SIGNUP_SIGNUP_BUTTON

class TestRegistration:
    def test_signup_correct_data(self, driver):
        driver.get('https://stellarburgers.education-services.ru/') 
        
        button = driver.find_element(By.XPATH, HOME_LOGIN_BUTTON)
        button.click()
        
        button = driver.find_element(By.XPATH, LOGIN_SIGNUP_LINK)
        button.click()

        name = driver.find_elements(By.XPATH, SIGNUP_NAME_INPUT)[0]
        name.send_keys(SIGNUP_NAME)

        email = driver.find_elements(By.XPATH, SIGNUP_NAME_INPUT)[1]
        email.send_keys(SIGNUP_EMAIL) 

        pswd = driver.find_element(By.XPATH, SIGNUP_PAROL_INPUT)
        pswd.send_keys(SIGNUP_PSWD) 
        
        button = driver.find_element(By.XPATH, SIGNUP_SIGNUP_BUTTON)
        button.click()

        sleep(1)

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.education-services.ru/login'

        driver.quit()

    def test_signup_wrong_pswd(self, driver):
        driver.get('https://stellarburgers.education-services.ru/') 
        
        button = driver.find_element(By.XPATH, HOME_LOGIN_BUTTON)
        button.click()
        
        button = driver.find_element(By.XPATH, LOGIN_SIGNUP_LINK)
        button.click()

        name = driver.find_elements(By.XPATH, SIGNUP_NAME_INPUT)[0]
        name.send_keys(SIGNUP_NAME)

        email = driver.find_elements(By.XPATH, SIGNUP_NAME_INPUT)[1]
        email.send_keys(SIGNUP_EMAIL) 

        pswd = driver.find_element(By.XPATH, SIGNUP_PAROL_INPUT)
        pswd.send_keys('012') 
        
        button = driver.find_element(By.XPATH, SIGNUP_SIGNUP_BUTTON)
        button.click()

        sleep(1)

        error = driver.find_element(By.XPATH, SIGNUP_PAROL_ERROR)
        error.text
        assert error.text == 'Некорректный пароль'


        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.education-services.ru/register'

        driver.quit()


        