import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utilities.config import Config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Browser from command line")
    parser.addoption("--headless", action="store_true", default=False)

@pytest.fixture(scope="function", autouse=True)
def setup_teardown(request):

    browser = request.config.getoption("--browser")

    if not browser:
        browser = Config.get_browser()

    print(f"Browser from CLI: {browser}")
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "edge":
        options = EdgeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}. "
                         f"Use --browser chrome, --browser firefox, "
                         f"or --browser edge")

    options.add_argument("--start-maximized")
    if request.config.getoption("--headless"):
        options.add_argument("--headless")

    if browser == "chrome":
        request.cls.driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        request.cls.driver = webdriver.Edge(options=options)
    elif browser == "firefox":
        request.cls.driver = webdriver.Firefox(options=options)

    request.cls.driver.maximize_window()

    yield
    request.cls.driver.quit()
