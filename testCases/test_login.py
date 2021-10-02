import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pageObjects.homePage import HomePage
from pageObjects.signInPage import SignInPage
from utilities import Utils
from utilities import LogGen

driver_path = Utils.select_webdriver_by_os_and_browser("chromedriver_ga")
fileLogName = os.path.abspath(__file__.replace(".py", ".log"))

if "/" in fileLogName:
    fileLogName = os.path.split(fileLogName)[1]
scriptPath = os.path.abspath(os.path.dirname(__file__))
os.chdir(scriptPath)

logger = LogGen.create_log_file_handler(os.path.join(scriptPath, LogGen.cleanupLogFileName(fileLogName)))

browser = "Chrome"
startUrl = "http://automationpractice.com/index.php"
email = "test999test@test.com"
password = "test999test"

def test_Login(caplog):
    # select log level
    caplog.set_level(logging.INFO)

    # Step 1 Set up general config and go to the start Page
    driver = Utils.setUpTest(logger, browser, driver_path, startUrl)

    # Step 2: click on the Sign In
    home = HomePage(driver)
    Utils.checkCondition(logger, home.click_on_locator(logger, home.signIn_link_linktext), "Click success",
                         "Click failed", driver)
    # check if current page equal expected page
    currentPageTitle = driver.title
    expectedPageTitle = "Login - My Store"
    Utils.checkCondition(logger, currentPageTitle == expectedPageTitle, "Current page is equal expected page",
                         "Current page isn't equal expected page", driver)

    # Step 3: Enter email and password and click submit btn(Sign In)
    login = SignInPage(driver)
    Utils.checkCondition(logger, login.enter_text(logger, login.emailToSignIn_textbox_id, email),
                         "Email was entered successful", "Email was entered successful", driver)
    Utils.checkCondition(logger, login.enter_text(logger, login.passwdToSignIn_textbox_id, password),
                         "Password was entered successful", "Password was entered successful", driver)
    Utils.checkCondition(logger, login.click_on_locator(logger, login.submitLogin_btn_id),
                         "Click success", "Click success", driver)

    # check if current page equal expected page(My account)
    currentPageTitle = driver.title
    expectedPageTitle = "My account - My Store"
    Utils.checkCondition(logger, currentPageTitle == expectedPageTitle, "Current page is equal expected page",
                         "Current page isn't equal expected page", driver)





    logger.info("Test Passed")
    Utils.finishTest(logger, driver)






