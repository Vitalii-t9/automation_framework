from pageObjects.pagePattern.basePage import BasePage


class ProdItemPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.addToCart_btn_xpath = "//span[contains(text(),'Add to cart')]"
        self.cart_link_xpath = "//header/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]"
        self.proceedToCheckout_btn_xpath = "//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]"
        self.continueShoping_btn_xpath = "//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/span[1]/span[1]"
        self.closePopUpAddToCart_btn_xpath = "//header/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/span[1]"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                             "css selector"]
