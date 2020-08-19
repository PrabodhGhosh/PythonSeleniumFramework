from datetime import datetime
import os
import pytest
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from jproperties import Properties

driver = None

pytest_plugins = [
   "data.testdata.InvalidLoginData"
  ]

@pytest.fixture(scope="class")

def setUp(request):
    global driver
    configs = Properties()
    with open("data/appdata.properties", "rb") as config_file:
        configs.load(config_file)
    driver = webdriver.WebDriver(ChromeDriverManager().install())
    driver.get(configs.get("URL")[0])
    driver.maximize_window()
    driver.implicitly_wait(configs.get("ImplicitWait")[0])
    request.cls.driver = driver
    request.cls.configs = configs
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":

        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = os.path.abspath(os.curdir)+"\\Screenshots\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+ ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists(os.path.abspath(os.curdir)+"\\reports"):
        os.makedirs(os.path.abspath(os.curdir)+"\\reports")
    config.option.htmlpath = (
        "reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )