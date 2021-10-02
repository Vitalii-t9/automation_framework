from pageObjects.pagePattern.basePage import BasePage

class CartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.home_link_xpath = "//div[@id='columns']/div/a/i"
        self.qtyItemPlus_link_selector = "i.icon-plus"
        self.qtyItemMinus_link_xpath = "//td[5]/div/a/span"
        self.removeItem_btn_selector = "i.icon-trash"
        self.continueShop_link_linktext = "Continue shopping"
        self.proceedToCheckout_link_linktext = "Proceed to checkout"
        self.prodDetView_link_xpath = "//td/a/img"
        self.summaryProductsQuantity_text_id = "summary_products_quantity"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]


