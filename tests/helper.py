from time import sleep
from tests.config import TEST_URL
from tests.testdata import SIGNUP_PSWD
from tests.locators import HEADER_KONSTR_LINK, HOME_LOGIN_BUTTON, HOME_ORDER_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, SIGNUP_PAROL_INPUT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support.expected_conditions import visibility_of_element_located

from tests.testdata import LOGIN_EMAIL


def login(driver):
    driver.get(TEST_URL) 
        
    button = driver.find_element(By.XPATH, HOME_LOGIN_BUTTON)
    button.click()

    email = driver.find_element(By.XPATH, LOGIN_EMAIL_INPUT)
    email.send_keys(LOGIN_EMAIL) 

    pswd = driver.find_element(By.XPATH, SIGNUP_PAROL_INPUT)
    pswd.send_keys(SIGNUP_PSWD) 
    
    button = driver.find_element(By.XPATH,LOGIN_LOGIN_BUTTON)
    button.click()

    WebDriverWait(driver, 3).until(visibility_of_element_located((By.XPATH, HOME_ORDER_BUTTON)))


def wait_for(driver, locator = HEADER_KONSTR_LINK):
    WebDriverWait(driver, 3).until(visibility_of_element_located((By.XPATH, locator )))
   