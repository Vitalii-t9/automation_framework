from pageObjects.pagePattern.basePage import BasePage


class SignInPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.emailToCreateAnAccount_textbox_id = "email_create"
        self.createAnAccountSubmitbtn_btn_id = "SubmitCreate"
        self.emailToSignIn_textbox_id = "email"
        self.passwdToSignIn_textbox_id = "passwd"
        self.forgotPasswd_link_linktext = "Forgot your password?"
        self.submitLogin_btn_id = "SubmitLogin"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]



