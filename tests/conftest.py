from random import randint
import pytest
from selenium import webdriver 

SIGNUP_NAME = "Елена Костюкова Тест"

SIGNUP_EMAIL = f"elena_kostyukova_35_{randint(100,999)}@mail.ru"
LOGIN_EMAIL = "elena_kostyukova_35_111@mail.ru"

SIGNUP_PSWD = "123456"

@pytest.fixture
def driver():
    return webdriver.Chrome()