from utility.base import BaseClass
from selenium.webdriver import Chrome
from jproperties import Properties


class TestHomePage(BaseClass):
    driver: Chrome
    configs:Properties

    def test_homepage(self):
        logger = BaseClass.getLogger(self)
        logger.info("Landed to homepage")
        assert self.driver.current_url, self.configs.get("URL")[0]
