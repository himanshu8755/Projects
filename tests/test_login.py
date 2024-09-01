import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    driver.get("http://example.com/login")
    login_page.login("test_user", "password123")
    assert "Dashboard" in driver.title
