import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()