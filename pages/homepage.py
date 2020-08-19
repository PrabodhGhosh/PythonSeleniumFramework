from selenium.webdriver import Chrome
from pages.loginpage import LogInPage


class HomePage:
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver

    #Page elements
    def signInBtn(self):
        return self.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")

    #Actions
    def clickSignIn(self):
        self.signInBtn().click()
        return LogInPage(self.driver)
