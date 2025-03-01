import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from pageObjects.homePage import HomePage
from utilities.readProperties import readConfig
from utilities.utils import Logger
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from tenacity import retry, stop_after_attempt, wait_fixed

base_url = readConfig.get_base_url()
user_name = readConfig.get_user_name()
password = readConfig.get_password()


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
@pytest.fixture(scope="class")
def setup_and_teardown_cls(request, browser, headless):
    customLogger = Logger.sample_logger()
    driver = None
    opt = ChromeOptions()
    edge_opt = EdgeOptions()

    try:
        if headless:
            opt.add_argument("--headless")
            edge_opt.add_argument("--headless")
            customLogger.info(" Headless Argument Added")
            customLogger.info(" Test Setup Started in Headless Mode")
        else:
            customLogger.info(" Headless Argument Not Provided ")
            customLogger.info(" Test Setup Started in Foreground with UI and not headless Mode")
        if browser == "chrome":
            driver = webdriver.Chrome(options=opt)
            print(driver.current_url)
        elif browser == "edge":
            driver = webdriver.Edge(options=edge_opt)
        else:
            customLogger.info( " Only Edge and Chrome Supported for cross-browser testing ")
            raise Exception
        home = HomePage(driver)
        driver.get(base_url)
        customLogger.info("***** Website Opened *****")
        driver.maximize_window()
        customLogger.info("***** Browser Window Maximized *****")
        home.enter_username(user_name)
        home.enter_password(password)
        dashboard = home.click_login_button()
        admin = dashboard.click_admin_side_menu()
        customLogger.info("***** Setup Done *****")
        request.cls.driver = driver
        request.cls.home = home
        request.cls.dashboard = dashboard
        request.cls.admin = admin
        request.cls.customLogger = customLogger

    except Exception as e:
        customLogger.exception("During the Test Setup an exception occurred.")
        customLogger.exception(str(e))
        raise e

    yield
    try:
        driver.quit()
        customLogger.info("Test Session Ended Successfully")
    except Exception as e:
        customLogger.exception("During the Test teardown an exception occurred.")
        customLogger.exception(str(e))
        raise e

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless", action="store_true")



@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def headless(request):
    return request.config.getoption("--headless")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):  # config comes from pytest.ini
    report_dir = "reports"
    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S %p")
    config.option.htmlpath = f"../{report_dir}/reports_{now}.html"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    test_name = item.name
    if report.when == "call":
        extra.append(pytest_html.extras.url(base_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S %p")
            file_name = test_name + now + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            item.cls.driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Orange HRM Test Report"
