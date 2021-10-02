import time
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pageObjects.homePage import HomePage
from pageObjects.prodItemPage import ProdItemPage
from utilities import Utils
from utilities import LogGen

driver_path = Utils.select_webdriver_by_os_and_browser("chromedriver_ga")
fileLogName = os.path.abspath(__file__.replace(".py", ".log"))

if "/" in fileLogName:
    fileLogName = os.path.split(fileLogName)[1]
scriptPath = os.path.abspath(os.path.dirname(__file__))
os.chdir(scriptPath)
logger = LogGen.create_log_file_handler(os.path.join(scriptPath, LogGen.cleanupLogFileName(fileLogName)))
logLevel = logging.INFO
browser = "Chrome"
startUrl = "http://automationpractice.com/index.php"


def test_AddItemToCart(caplog):
    # select log level
    caplog.set_level(logging.INFO)

    # Step 1 Set up general config and go to the start Page
    driver = Utils.setUpTest(logger, browser, driver_path, startUrl)

    # Step 2: click on any item then compare current page title with expected
    home = HomePage(driver)
    Utils.checkCondition(logger, home.click_on_locator(logger, home.prodItem1_link_xpath), "Click success",
                         "Click Failed", driver)
    time.sleep(2)
    currentPageTitle = driver.title
    expectedPageTitle = "Faded Short Sleeve T-shirts - My Store"
    Utils.checkCondition(logger, currentPageTitle == expectedPageTitle, "Current page is equal expected page",
                         "Current page isn't equal expected page", driver)

    # Step 3: click add item to Cart
    item = ProdItemPage(driver)
    Utils.checkCondition(logger, item.click_on_locator(logger, item.addToCart_btn_xpath), "Click success",
                         "Click failed", driver)
    # close popup
    Utils.checkCondition(logger, item.click_on_locator(logger, item.closePopUpAddToCart_btn_xpath), "Click success",
                         "Click failed", driver)

    # Step 5: Go to Cart and check is added item there
    Utils.checkCondition(logger, item.click_on_locator(logger, item.cart_link_xpath), "Click success",
                         "Click failed", driver)
    time.sleep(2)
    # compare current page title with expected
    currentPageTitle = driver.title
    expectedPageTitle = "Order - My Store"
    Utils.checkCondition(logger, currentPageTitle == expectedPageTitle, "Current page is equal expected page",
                         "Current page isn't equal expected page", driver)

    # check if item was added to cart
    currentItemQnt = driver.find_element_by_id("summary_products_quantity").text
    expectedItemQnt = "1 Product"
    Utils.checkCondition(logger, currentItemQnt == expectedItemQnt, "Current Qtn is equal expected Qtn",
                         "Current Qtn isn't equal expected Qtn", driver)

    logger.info("Test Passed")
    Utils.finishTest(logger, driver)






