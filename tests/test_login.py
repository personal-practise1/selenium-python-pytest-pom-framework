from page_objects.login_page import LoginPage
from utilities.config import Config
from utilities.logger import get_logger

log = get_logger()
class TestLogin:

    def test_login(self):
        self.driver.get(Config.get_url())

        login_page = LoginPage(self.driver)

        login_page.login(Config.get_username(),
                         Config.get_password())
        log.info("logged in")