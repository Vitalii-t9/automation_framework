from pageObjects.pagePattern.basePage import BasePage

class ContactUs(BasePage):

    def __init__(self, driver):

        self.driver = driver
        # user is log ina
        self.contactUs_link_linktext = "Contact us"
        self.subjectHeading_dropdownmenu_id = "id_contact"
        self.subjectHeading_dropdownmenuitem_visibletext = "Customer service"
        self.email_textbox_id = "email"
        self.orderReference_dropdownmenu_name = "id_order"
        self.orderReference_dropdownmenuitem_visibletext = "EHITPLQFI - 08/18/2021"
        self.product_dropdownmenu_id = "352593_order_products"
        self.product_dropdownmenuitem_visibletext = "Printed Dress - Color : Orange, Size : S"
        self.attachFile_uploader_xpath = "//div[@id='uniform-fileUpload']/span[2]"
        self.message_textbox_id = "message"
        self.send_btn_xpath = "//button[@id='submitMessage']/span"
        # user is log out
        self.orderReference_textbox_id = "id_order"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]



