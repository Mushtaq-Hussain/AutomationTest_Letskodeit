from base.selenium_driver import SeleniumDriver
import utilities.Custom_logger as cl
import logging
import time


class LoginPage(SeleniumDriver):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_btn = "commit"

# find and get locators
#     def get_login_link(self):
#         return self.driver.find_element(By.LINK_TEXT, self._login_link)
#
#     def get_email_field(self):
#         return self.driver.find_element(By.ID, self._email_field)
#
#     def get_password_field(self):
#         return self.driver.find_element(By.ID, self._password_field)
#
#     def get_login_button(self):
#         return self.driver.find_element(By.NAME, self._login_btn)

# Operation on locators
    def click_on_login_link(self):
        self.elementClick(self._login_link, locatorType= "link")

    def enter_email(self, email):
        self.sendKeys(email, self._email_field)

    def enter_password(self, password):
        self.sendKeys(password, self._password_field)

    def click_login_button(self):
        self.elementClick(self._login_btn, locatorType= "name")

    def login_test(self, email="", password=""):
        self.click_on_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(60)


    def valid_login(self):
        result = self.isElementPresent("//span[contains(text(),'Test Account')]", locatorType= "xpath")
        return result

    def invalid_login(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password.')]",locatorType="xpath")
        return result