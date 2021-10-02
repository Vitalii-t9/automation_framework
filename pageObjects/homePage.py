from pageObjects.pagePattern.basePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.signIn_link_linktext = "Sign in"
        self.contactUs_link_linktext = "Contact us"
        self.search_textbox_id = "search_query_top"
        self.submitSerch_Btn_name = "submit_search"
        self.cart_link_cssselectors = ".shopping_cart a"
        self.womanCatg_link_linktext = "Women"
        self.dressesCatg_link_xpath = "//div[@id='block_top_menu']/ul/li[2]/a"
        self.tshirtsCatg_link_xpath = "//div[@id='block_top_menu']/ul/li[3]/a"
        self.prevBtnHomeSlider_btn_classname = "bx-prev"
        self.nextBtnHomeSlider_btn_classname = "bx-next"
        self.popular_link_classname = "homefeatured"
        self.bestsellers_link_classname = "blockbestsellers"
        self.prodItem1_link_xpath = "//body/div[@id='page']/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/h5[1]/a[1]"
        self.prodItem2_link_xpath = "//img[@alt='Printed Dress']"
        self.prodItemQuickView_link_classname = "quick-view-mobile"
        self.prodItemCloseQuickView_classname = "fancybox-close"
        self.addToCartQuickView_btn_classname = "exclusive"
        self.prodDeteilView_link_linktext = "More"
        self.addToCart_btn_xpath = "//ul[@id='homefeatured']/li[2]/div/div[2]/div[2]/a/span"
        self.closeAddToCartPopUp_btn_cssselector = "span.cross"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]




