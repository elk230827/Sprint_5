from os import error
from time import sleep
from selenium.webdriver.common.by import By

from tests.conftest import LOGIN_EMAIL, SIGNUP_EMAIL, SIGNUP_NAME, SIGNUP_PSWD
from tests.helper import login
from tests.locators import HEADER_KONSTR_LINK, HEADER_LK_LINK, HOME_BUN_BUTTON, HOME_BUN_HDR, HOME_FILL_BUTTON, HOME_FILL_HDR, HOME_LOGIN_BUTTON, HOME_ORDER_BUTTON, HOME_SAUSE_BUTTON, HOME_SAUSE_HDR, LK_EXIT_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, LOGIN_RECOVERY_BUTTON, LOGIN_SIGNUP_LINK, RECOVERY__LOGIN_BUTTON, SIGNUP_LOGIN_BUTTON, SIGNUP_NAME_INPUT, SIGNUP_PAROL_ERROR, SIGNUP_PAROL_INPUT, SIGNUP_SIGNUP_BUTTON


from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

class TestKonstr:
    def test_bun_konst_after_login(self, driver):
        login(driver)


        button = driver.find_element(By.XPATH,HOME_BUN_BUTTON)
        ActionChains(driver)\
            .move_to_element(button)\
            .click()\
            .perform()


        sleep(1)

        h = driver.find_element(By.XPATH,HOME_BUN_HDR)
        assert h.is_displayed()
        driver.quit()


    def test_sause_konst_after_login(self, driver):
        login(driver)


        button = driver.find_element(By.XPATH,HOME_SAUSE_BUTTON)
        ActionChains(driver)\
            .move_to_element(button)\
            .click()\
            .perform()


        sleep(1)

        h = driver.find_element(By.XPATH,HOME_SAUSE_HDR)
        assert h.is_displayed()
        driver.quit()

    def test_fill_konst_after_login(self, driver):
        login(driver)


        button = driver.find_element(By.XPATH,HOME_FILL_BUTTON)
        ActionChains(driver)\
            .move_to_element(button)\
            .click()\
            .perform()


        sleep(1)

        h = driver.find_element(By.XPATH,HOME_FILL_HDR)
        assert h.is_displayed()
        driver.quit()       
    