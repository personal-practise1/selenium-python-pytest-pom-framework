import pytest
from page_objects.login_page import LoginPage
from test_data.login_data import login_data
from utilities.config import Config
from utilities.logger import get_logger

log = get_logger()
class TestLogin:

    @pytest.mark.parametrize("username, password",login_data)
    def test_login(self, username, password):
        self.driver.get(Config.get_url())

        login_page = LoginPage(self.driver)

        login_page.login(username, password)
        log.info(login_page.get_title())
        log.info("logged in")