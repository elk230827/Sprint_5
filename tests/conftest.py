import pytest
from selenium import webdriver 

TEST_URL = 'https://stellarburgers.education-services.ru'

@pytest.fixture
def driver():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit()