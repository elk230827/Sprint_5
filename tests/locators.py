HEADER_LK_LINK = '//p[contains(text(), "Личный Кабинет")]' 
HEADER_KONSTR_LINK = '//p[contains(text(), "Конструктор")]'
HEADER_LOGO_LINK = '//a[@href="/"]'

HOME_LOGIN_BUTTON = '//button[contains(text(), "Войти в аккаунт")]'
HOME_ORDER_BUTTON = '//button[contains(text(), "Оформить заказ")]'
HOME_BUN_BUTTON = '//div[span[contains(text(), "Булки")]]'
HOME_BUN_SELECTED = '//div[span[contains(text(), "Булки")] and contains(@class, "tab_tab_type_current")]'
HOME_SAUSE_BUTTON = '//div[span[contains(text(), "Соусы")]]'
HOME_SAUSE_SELECTED = '//div[span[contains(text(), "Соусы")] and contains(@class, "tab_tab_type_current")]'
HOME_FILL_BUTTON = '//div[span[contains(text(), "Начинки")]]'
HOME_FILL_SELECTED = '//div[span[contains(text(), "Начинки")] and contains(@class, "tab_tab_type_current")]'


LOGIN_SIGNUP_LINK = '//a[contains(text(), "Зарегистрироваться")]'
LOGIN_EMAIL_INPUT = '//input[@name="name"]'
LOGIN_LOGIN_BUTTON = '//button[contains(text(), "Войти")]'
LOGIN_RECOVERY_BUTTON = '//a[contains(text(), "Восстановить пароль")]'

SIGNUP_NAME_INPUT = '//input[@name="name"]'
SIGNUP_PAROL_INPUT = '//input[@name="Пароль"]'
SIGNUP_SIGNUP_BUTTON = '//button[contains(text(), "Зарегистрироваться")]'
SIGNUP_PAROL_ERROR = '//p[contains(@class, "input__error")]'
SIGNUP_LOGIN_BUTTON = '//a[contains(text(), "Войти")]'

RECOVERY__LOGIN_BUTTON = '//a[contains(text(), "Войти")]'

LK_EXIT_BUTTON = '//button[contains(text(), "Выход")]'
LK_PROFILE_BUTTON = '//a[contains(text(), "Профиль")]'
