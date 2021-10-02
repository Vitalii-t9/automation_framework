from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self):
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    def click_on_locator(self, logger, locator):
        dictionary = self.__dict__
        try:
            for locatorType in self.locatorTypes:
                if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
                    self.driver.find_element(locatorType, locator).click()
                    logger.info(f"locator type '{locatorType}' locator '{locator}' was found")
                    return True
        except NoSuchElementException:
            logger.error(f"locator '{locator}' was not found on the page!!!")
            return False 
               
    def select_by_visibletext(self, logger, locator, visible_text):
        dictionary = self.__dict__
        try:
            if self.find_name(dictionary, locator)[-2] == "dropdownmenu":
                for locatorType in self.locatorTypes:
                    if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
                        self.driver.find_element(locatorType, locator).click()
                        Select(self.driver.find_element(locatorType, locator)).select_by_visible_text(visible_text)
                        logger.info(f"locator type '{locatorType}' locator '{locator}'\
                         was found and selected by visible text successful")
                        return True
        except NoSuchElementException:
            logger.error(f"locator '{locator}' was not found on the page!!!")
            return False 
            
    def enter_text(self, logger, locator, text):
        dictionary = self.__dict__
        try:
            if self.find_name(dictionary, locator)[-2] == "textbox":
                for locatorType in self.locatorTypes:
                    if self.find_name(dictionary, locator)[-1] == locatorType.replace(" ", ""):
                        self.driver.find_element( locatorType, locator).clear()
                        logger.info(f" text box with locator type '{locatorType}' locator '{locator}' was cleared successful")
                        self.driver.find_element(locatorType, locator).send_keys(text)
                        logger.info(f"enter text in the text box with locator type '{locatorType}' locator '{locator}'")
                        return True
        except NoSuchElementException:
            logger.error(f"locator '{locator}' was not found on the page!!!")
            return False 
    
    def find_name(self, dic, locator):
        for k, v in dic.items():
            if dic[k] == locator:
                return k.split("_")


