import pytest
from selenium import webdriver
from sbis import SbisPage

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    main_page = SbisPage(driver)
    main_page.go_to_site()
    yield main_page
    driver.quit()