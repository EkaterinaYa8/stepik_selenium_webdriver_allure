from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import re


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.fill_in_field(*LoginPageLocators.REGISTRATION_USER_NAME, email)
        self.fill_in_field(*LoginPageLocators.REGISTRATION_PASSWORD_1, password)
        self.fill_in_field(*LoginPageLocators.REGISTRATION_PASSWORD_2, password)
        self.click_on_element(*LoginPageLocators.REGISTRATION_BUTTON)

    def login(self, email, password):
        self.fill_in_field(*LoginPageLocators.LOGIN_USER_NAME, email)
        self.fill_in_field(*LoginPageLocators.LOGIN_PASSWORD, password)
        self.click_on_element(*LoginPageLocators.LOGIN_BUTTON)

    def should_be_login_icon(self):
        self.is_element_present(*BasePageLocators.USER_ICON)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_in_url_list = re.findall(r'accounts/(\w+)', self.browser.current_url)

        assert len(login_in_url_list) == 1, \
            'URL страницы входа и регистрации должен содержать в конце login.' \
            'Ошибка парсинга URL на наличие "login" после "accounts/".\n' \
            'Ожидается, что URL содержит в конце строку формата: "accounts/[A-Z]", возможно, URL был изменён.'

        assert login_in_url_list[0] == 'login', 'URL страницы входа и регистрации должен содержать в конце login.'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода email в форме авторизации.'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода пароля в форме авторизации.'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
            'На странице "Войти или зарегистрироваться" отсутствует кнопка для входа пользователя.'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USER_NAME), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода email в форме регистрации.'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для ввода пароля в форме регистрации.'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), \
            'На странице "Войти или зарегистрироваться" отсутствует поле для повторного ввода пароля в форме регистрации.'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), \
            'На странице "Войти или зарегистрироваться" отсутствует кнопка подтверждения регистрации.'

    def should_be_success_register_message(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS_MSG), \
            'После регистрации нового пользователя с уникальным email должно появиться сообщение об успешной ' \
            'регистрации. Сообщение отсуствует.'
