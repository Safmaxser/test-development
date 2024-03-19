import pytest
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
PHONE = os.getenv('PHONE')


class TestAuthorizationYandex:
    def _wait_element(self, delay_second=1, by=By.CLASS_NAME, value=None):
        return WebDriverWait(self.browser, delay_second).until(
            expected_conditions.presence_of_element_located((by, value)))

    def _browser_chrome_init(self):
        chrome_path = ChromeDriverManager().install()
        browser_service = Service(executable_path=chrome_path)
        self.browser = Chrome(service=browser_service)

    def setup_method(self):
        self._browser_chrome_init()

    def test_authorization_mail_form(self):
        self.browser.get('https://passport.yandex.ru/auth/')
        assert self.browser.title == 'Авторизация'
        button_mail_form = self._wait_element(
            1, By.CLASS_NAME, 'Button2.Button2_checked.Button2_size_l.'
                              'Button2_view_default')
        if button_mail_form.text != 'Почта':
            button_telephone_form = self._wait_element(
                1, By.CLASS_NAME, 'Button2.Button2_size_l.Button2_view_clear')
            button_telephone_form.click()
        input_login = self._wait_element(1, By.ID, 'passp-field-login')
        input_login.clear()
        input_login.send_keys(LOGIN)
        button_next = self.browser.find_element(by=By.ID,
                                                value='passp:sign-in')
        button_next.click()
        input_password = self._wait_element(1, By.ID, 'passp-field-passwd')
        assert (self.browser.current_url ==
                'https://passport.yandex.ru/auth/welcome')
        input_password.clear()
        input_password.send_keys(PASSWORD)
        button_next = self.browser.find_element(by=By.ID,
                                                value='passp:sign-in')
        button_next.click()
        sleep(5)
        assert self.browser.current_url == 'https://id.yandex.ru/'

    def test_authorization_phone_form(self):
        self.browser.get('https://passport.yandex.ru/auth/')
        assert self.browser.title == 'Авторизация'
        button_active_form = self._wait_element(
            1, By.CLASS_NAME, 'Button2.Button2_checked.Button2_size_l.'
                              'Button2_view_default')
        if button_active_form.text != 'Телефон':
            button_phone_form = self._wait_element(
                1, By.CLASS_NAME, 'Button2.Button2_size_l.Button2_view_clear')
            button_phone_form.click()
        input_phone = self._wait_element(1, By.ID, 'passp-field-phone')
        input_phone.clear()
        input_phone.send_keys(PHONE)
        button_next = self.browser.find_element(by=By.ID,
                                                value='passp:sign-in')
        button_next.click()
        sleep(5)
        assert (self.browser.current_url ==
                'https://passport.yandex.ru/auth/reg')
