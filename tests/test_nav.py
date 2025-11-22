from helper import wait_for
from os import error
from time import sleep
from selenium.webdriver.common.by import By

from tests.config import TEST_URL
from tests.testdata import SIGNUP_PSWD
from tests.helper import login
from tests.locators import HEADER_KONSTR_LINK, HEADER_LK_LINK, HEADER_LOGO_LINK, HOME_LOGIN_BUTTON, HOME_ORDER_BUTTON, LK_EXIT_BUTTON, LK_PROFILE_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, LOGIN_RECOVERY_BUTTON, LOGIN_SIGNUP_LINK, RECOVERY__LOGIN_BUTTON, SIGNUP_LOGIN_BUTTON, SIGNUP_NAME_INPUT, SIGNUP_PAROL_ERROR, SIGNUP_PAROL_INPUT, SIGNUP_SIGNUP_BUTTON
from tests.testdata import LOGIN_EMAIL, SIGNUP_EMAIL, SIGNUP_NAME

class TestNav:
    def test_lk_after_login(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()

        wait_for(driver, LK_PROFILE_BUTTON)

        current_url = driver.current_url
        assert current_url == f'{TEST_URL}/account/profile'
        


    def test_konstr_after_lk(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()
        wait_for(driver, LK_PROFILE_BUTTON)

        button = driver.find_element(By.XPATH,HEADER_KONSTR_LINK)
        button.click()


        current_url = driver.current_url
        assert current_url.strip("/") == TEST_URL
        
    

    def test_logo_after_lk(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()
        wait_for(driver, LK_PROFILE_BUTTON)


        button = driver.find_element(By.XPATH,HEADER_LOGO_LINK)
        button.click()

        current_url = driver.current_url
        assert current_url.strip("/") == TEST_URL
               

    def test_exit_after_lk(self, driver):
        login(driver)
        button = driver.find_element(By.XPATH,HEADER_LK_LINK)
        button.click()
        
        wait_for(driver, LK_PROFILE_BUTTON)

        button = driver.find_element(By.XPATH,LK_EXIT_BUTTON)
        button.click()

        wait_for(driver, LOGIN_LOGIN_BUTTON)

        current_url = driver.current_url
        assert current_url.strip("/") == f'{TEST_URL}/login'
        

                
   