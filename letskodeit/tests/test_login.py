from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login_test("test@email.com", "abcabc")
        result = self.lp.valid_login()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
         self.lp.login_test("test@email.com", "abcabcabac")
         result = self.lp.invalid_login()
         assert result == True



