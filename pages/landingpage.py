from selenium.webdriver import Chrome

class LandingPage:
    driver: Chrome

    def __init__(self, driver):
        self.driver = driver

    # Page elements
    def signOut(self):
        return self.driver.find_element_by_class_name("logout")

    # Actions
    def verifyLogOutPresence(self):
        return self.signOut().is_displayed()