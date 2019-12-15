from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    VIEW_BASKET_BUTTON = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]/span[@class="btn-group"]')
    USER_ICON = (By.XPATH, '//i[@class="icon-user"]')


class MainPageLocators():
    ALL_PRODUCTS_LINK = (By.XPATH, '//li[@class="dropdown active open"]/ul[@class="dropdown-menu"]/li[1]/a[@href]')


class LoginPageLocators():
    LOGIN_USER_NAME = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@name="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')

    REGISTRATION_USER_NAME = (By.XPATH, '//input[@name="registration-email"]')
    REGISTRATION_PASSWORD_1 = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTRATION_PASSWORD_2 = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
    REGISTRATION_SUCCESS_MSG = (By.XPATH, '//div[@class="alert alert-success  fade in"]')
