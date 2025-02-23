import pytest

from pageObjects.account_page import AccountPage
from pageObjects.contact_page import ContactPage
from pageObjects.lead_page import LeadPage
from pageObjects.login_page import LoginPage
from pageObjects.opportunity_page import OpportunitiesPage
from driver import get_driver


@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    # driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def lead_page(driver):
    return LeadPage(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def contact_page(driver):
    return ContactPage(driver)


@pytest.fixture
def opportunity_page(driver):
    return OpportunitiesPage(driver)
