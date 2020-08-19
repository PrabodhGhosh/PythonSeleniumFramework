import time

from pages.homepage import HomePage
from utility.base import BaseClass
from selenium.webdriver import Chrome


class TestLogin(BaseClass):
    driver: Chrome

    def test_login(self):
        homepage = HomePage(self.driver)
        #Hold the LoginPage instance
        loginpage=homepage.clickSignIn()
        loginpage.enterEmail("suhanapiku@gmail.com")
        loginpage.enterPassword("abcd1234")
        #Hold the landing page instance
        landingpage = loginpage.clickSigIn()
        assert landingpage.verifyLogOutPresence()
