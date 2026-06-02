import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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

    # Required for GitHub Actions/Linux
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")

    if browser == "chrome":
        request.cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    elif browser == "edge":
        request.cls.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    elif browser == "firefox":
        request.cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

    request.cls.driver.maximize_window()

    yield
    request.cls.driver.quit()
