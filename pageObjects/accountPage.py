from pageObjects.pagePattern.basePage import BasePage

class AccountPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.account_link_xpath = "//header[@id='header']/div[2]/div/div/nav/div/a/span"
        self.home_link_xpath = "//div[@id='columns']/div/a/i"
        self.orderHistAndAccount_link_xpath = "//div[@id='center_column']/div/div/ul/li/a/span"
        self.myWishList_link_xpath = "//div[@id='center_column']/div/div[2]/ul/li/a/span"
        self.myCreditSlips_link_xpath = "//div[@id='center_column']/div/div/ul/li[2]/a/span"
        self.myAddress_link_xpath = "//div[@id='center_column']/div/div/ul/li[3]/a/span"
        self.myPersonalInfo_link_xpath = "//div[@id='center_column']/div/div/ul/li[4]/a/span"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]








