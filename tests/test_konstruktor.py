from os import error
from time import sleep
from selenium.webdriver.common.by import By

from tests.testdata import SIGNUP_PSWD
from tests.helper import login
from tests.locators import HEADER_KONSTR_LINK, HEADER_LK_LINK, HOME_BUN_BUTTON, \
    HOME_BUN_SELECTED, HOME_FILL_BUTTON, HOME_FILL_SELECTED, HOME_LOGIN_BUTTON, \
    HOME_ORDER_BUTTON, HOME_SAUSE_BUTTON, HOME_SAUSE_SELECTED, LK_EXIT_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, LOGIN_RECOVERY_BUTTON, LOGIN_SIGNUP_LINK, RECOVERY__LOGIN_BUTTON, SIGNUP_LOGIN_BUTTON, SIGNUP_NAME_INPUT, SIGNUP_PAROL_ERROR, SIGNUP_PAROL_INPUT, SIGNUP_SIGNUP_BUTTON


from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from tests.testdata import LOGIN_EMAIL, SIGNUP_EMAIL, SIGNUP_NAME

class TestKonstr:
    def test_bun_konst_after_login(self, driver):
        login(driver)

        # переключимся на Начинки, чтобы проверить булки 
        button = driver.find_element(By.XPATH, HOME_FILL_BUTTON)
        button.click()

        button = driver.find_element(By.XPATH, HOME_BUN_BUTTON)
        ActionChains(driver)\
            .move_to_element(button)\
            .click()\
            .perform()



        assert driver.find_element(By.XPATH, HOME_BUN_SELECTED).is_displayed()


    def test_sause_konst_after_login(self, driver):
        login(driver)


        button = driver.find_element(By.XPATH,HOME_SAUSE_BUTTON)
        ActionChains(driver)\
            .move_to_element(button)\
            .click()\
            .perform()

        assert driver.find_element(By.XPATH, HOME_SAUSE_SELECTED).is_displayed()

    def test_fill_konst_after_login(self, driver):
        login(driver)


        button = driver.find_element(By.XPATH, HOME_FILL_BUTTON)
        ActionChains(driver)\
            .move_to_element(button)\
            .click()\
            .perform()

        assert driver.find_element(By.XPATH, HOME_FILL_SELECTED).is_displayed()
       
    