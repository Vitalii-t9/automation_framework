from pageObjects.pagePattern.basePage import BasePage


class CreateAnAccountPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        # user pesonal information
        self.genderMr_radiobtn_id = "id_gender1"
        self.genderMrs_radiobtn_id = "id_gender2"
        self.userFirstName_textbox_id = "customer_firstname"
        self.userSecondName_textbox_id = "customer_lastname"
        self.userEmail_textbox_id = "email"
        self.userPasswd_textbox_id = "passwd"
        self.dayOfBirth_dropdownmenu_id = "days"
        self.dayOfBirth_menuitem_visibletext = "regexp:12\\s+"
        self.monthOfBirth_dropdownmenu_id = "months"
        self.monthOfBirth_menuitem_visibletext = "regexp:May\\s"
        self.yearOfBirth_dropdownmenu_id = "years"
        self.yearOfBirth_menuitem_visibletext = "regexp:2015\\s+"
        self.receiveNewsletter_checkbox_id = "newsletter"
        self.receiveSpecialoffers_checkbox_id = "optin"
        # user address
        self.firstNameDelivery_textbox_id = "firstname"
        self.lastNameDelivery_textbox_id = "lastname"
        self.companyName_textbox_id = "company"
        self.address_textbox_id = "address1"
        self.addressLine2_textbox_id = "address2"
        self.city_textbox_id = "city"
        self.state_dropdownmenu_id = "id_state"
        self.state_menuitem_visibletext = "Idaho"
        self.postCode_textbox_id = "postcode"
        self.contry_dropdownmenu_id = "id_country"
        self.additionalInformation_textbox_id = "other"
        self.mobilePhone_textbox_id = "phone_mobile"
        self.aliasForAddress_textbox_id = "alias"
        self.submitAccount_btn_id = "submitAccount"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]




