import sys
import time

from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger.add(sys.stderr, format="{time} {level} {message}", colorize=True, filter="my_module", level="INFO")
new_level = logger.level("START", no=38, color="<yellow>")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    @logger.catch
    def find_element(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    @logger.catch
    def find_elements(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")
    
    @logger.catch
    def find_p_elements(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    @logger.catch
    def go_to_site(self):
        logger.log("START", "NEW SESSION STARTED. OPENING LINK.")
        return self.driver.get(self.base_url)
    
    @logger.catch
    def go_to_window(self, number):
        window = self.driver.window_handles[number]
        self.driver.switch_to.window(window)
        time.sleep(3)
        return
    
    @logger.catch
    def get_url(self):
        """Gets url of current page."""
        logger.info(f"CURRENT URL RECIEVED: {self.driver.current_url}.")
        return self.driver.current_url
    
    @logger.catch
    def js_click(self, element):
        """Clicking with js code"""
        logger.info(f"Clicking with js code on element: {element}.")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        return
    
    @logger.catch
    def get_title(self):
        """Returns title of a page"""
        title = self.driver.title
        logger.info(f"Page title is: {title}.")
        return title
