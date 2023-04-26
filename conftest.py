import pytest
import random
import datetime
from selenium import webdriver


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def get_phone_number():
    return random.randint(79000000000, 79999999999)


@pytest.fixture
def get_date_today():
    return datetime.date.today().strftime('%d.%m.%Y')


@pytest.fixture
def get_date_tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')
