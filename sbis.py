import sys
import time
from loguru import logger
from selenium.webdriver.common.by import By
from base_app import BasePage


logger.add(sys.stderr, format='{time} {level} {message}', colorize=True, filter='my_module', level='INFO')
logger.add('log_file.log', level='TRACE', rotation='5 MB')

class SbisLocators:
    '''Locators for Sbis page'''
    SBIS_CONTACTS_BUTTON = (By.LINK_TEXT,'Контакты')
    SBIS_TENZOR_BANNER = (By.XPATH, '//a[@title="tensor.ru"]')
    TENZOR_HUMAN_POWER = (By.XPATH, '/HTML//*[text()="Сила в людях"]')
    TENZOR_ABOUT_LINK = (By.XPATH, '/HTML//div[@class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"]//a[@class="tensor_ru-link tensor_ru-Index__link"]')
    TENZOR_IMAGES = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]')
    SBIS_AREA = (By.CLASS_NAME, "sbis_ru-Region-Chooser")
    SBIS_PARTNERS = (By.CLASS_NAME, 'sbisru-Contacts-City__item')
    SBIS_41_AREA = (By.XPATH, '//*[@title="Камчатский край"]')

class SbisPage(BasePage):
    '''Class for interacting https://sbis.ru/ '''
    @staticmethod
    @logger.catch
    def click_on_it(element):
        logger.info("Mouse LF click.")
        element.click()
        time.sleep(7)
        return
    
    @logger.catch
    def click_on_it_js(self, element):
        logger.info("Browser js mouse LF click.")
        return self.js_click(element)
    
    @logger.catch
    def get_contacts_button(self):
        '''Go to contacts page'''
        logger.info('Getting contacts button')
        return self.find_element(SbisLocators.SBIS_CONTACTS_BUTTON)

    @logger.catch
    def get_tenzor_banner(self):
        '''Find tenzor banner in contacts page'''
        logger.info('Getting tenzor banner')
        return self.find_element(SbisLocators.SBIS_TENZOR_BANNER)
    
    @logger.catch
    def switch_windows(self, number):
        """Switching browser window to next."""
        logger.info('Browser tab was switched.')
        return self.go_to_window(number)
    
    @logger.catch
    def get_p_text(self):
        '''Find text from <p> tag contains Сила в людях'''
        logger.info('Getting <p> where text is "Сила в людях"')
        return self.driver.find_element(By.XPATH, '/HTML//*[text()="Сила в людях"]')
    
    @logger.catch
    def get_about_link(self):
        '''Getting link from block contains Сила в людях'''
        logger.info('Getting link from block contains "Сила в людях"')
        return self.find_element(SbisLocators.TENZOR_ABOUT_LINK)
    
    @logger.catch
    def get_images(self):
        '''Getting images from block Работаем'''
        logger.info('Getting images')
        div = self.find_element(SbisLocators.TENZOR_IMAGES)
        return div.find_elements(By.TAG_NAME, 'img')
        
    @logger.catch
    def get_area(self):
        '''Getting current area'''
        logger.info('Getting current area')
        return self.find_element(SbisLocators.SBIS_AREA)
        
    @logger.catch
    def get_partrers(self):
        '''Getting partner list'''
        logger.info('Getting partner list')
        return self.find_elements(SbisLocators.SBIS_PARTNERS)
    
    @logger.catch
    def choose_area(self):
        '''Finds 41 area'''
        logger.info('Finding 41 area')
        return self.find_element(SbisLocators.SBIS_41_AREA)
