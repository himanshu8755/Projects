from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')

    def login(self, username, password):
        self.find_element(*self.USERNAME).send_keys(username)
        self.find_element(*self.PASSWORD).send_keys(password)
        self.click(*self.LOGIN_BUTTON)
