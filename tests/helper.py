from time import sleep
from tests.conftest import LOGIN_EMAIL, SIGNUP_PSWD
from tests.locators import HOME_LOGIN_BUTTON, LOGIN_EMAIL_INPUT, LOGIN_LOGIN_BUTTON, SIGNUP_PAROL_INPUT
from selenium.webdriver.common.by import By


def login(driver):
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