import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pageObjects.homePage import HomePage
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


def test_SearchBox(caplog):
    # select log level
    caplog.set_level(logging.INFO)
    # Step 1 Set up general config and go to the start Page
    driver = Utils.setUpTest(logger, browser, driver_path, startUrl)
    # Step 2: enter some query to the search box
    home = HomePage(driver)
    query = "dress"
    Utils.checkCondition(logger, home.enter_text(logger, home.search_textbox_id, query),
                         f"query '{query}' was entered in the searchBox successful",
                         f"query '{query}' was not entered in the searchBox - failed", driver)


    # Step 3: click on the search button
    Utils.checkCondition(logger, home.click_on_locator(logger, home.submitSerch_Btn_name),
                         f"click search Btn successful",
                         f"click search Btn failed", driver)

    # Step 4: Check current page title with expected
    Utils.checkCondition(logger, driver.title == "Search - My Store", "Page checking success", "Page checking failed",
                         driver)

    logger.info("Test Passed")
    Utils.finishTest(logger, driver)






