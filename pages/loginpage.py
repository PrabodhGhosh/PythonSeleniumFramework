from selenium.webdriver import Chrome

from pages.landingpage import LandingPage


class LogInPage:
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver

    # Page elements
    def email(self):
        return self.driver.find_element_by_id("email")

    def password(self):
        return self.driver.find_element_by_id("passwd")

    def signIn(self):
        return self.driver.find_element_by_id("SubmitLogin")

    def errorMessage(self):
        return self.driver.find_element_by_xpath("//p[contains(text(),'There is 1 error')]")

    #Actions

    #Enter email
    def enterEmail(self, option):
        self.email().send_keys(option)

    # Enter password
    def enterPassword(self, option):
        self.password().send_keys(option)

    # Click sign in
    def clickSigIn(self):
        self.signIn().click()
        return LandingPage(self.driver)

    #verify error message

    def verifyErrorMsg(self):
        return self.errorMessage().is_displayed()