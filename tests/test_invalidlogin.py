import pytest
from pages.homepage import HomePage
from utility.base import BaseClass
from selenium.webdriver import Chrome


@pytest.mark.usefixtures("invalidLoginData")
class TestInvalidLogin(BaseClass):
    driver: Chrome

    def test_invalidLogin(self, invalidLoginData):
        logger = BaseClass.getLogger(self)
        homepage = HomePage(self.driver)
        # Hold the LoginPage instance
        loginpage = homepage.clickSignIn()
        logger.info("Clicked Sign In button")
        loginpage.enterEmail(invalidLoginData[0])
        logger.info("Entered email")
        loginpage.enterPassword(invalidLoginData[1])
        logger.info("Entered password")
        # Hold the landing page instance
        loginpage.clickSigIn()
        assert loginpage.verifyErrorMsg()
