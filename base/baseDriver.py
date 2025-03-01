from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Logger
from selenium.common import exceptions


class BaseDriver:
    customLogger = Logger.sample_logger()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url):
        return self.driver.get(url)

    def wait_for_element_to_be_visible(self, locator):
        self.customLogger.debug(msg=
                                "Waiting for Element to be visible with locator: {}".format(locator))
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.customLogger.info("Element found visible")
            return element
        except  exceptions.TimeoutException:
            self.customLogger.error("While waiting for element to be visible - Timeout Exception Occurred.")
        except  exceptions.ElementNotVisibleException:
            self.customLogger.error(
                "While waiting for element to be visible - ElementNotVisibleException Occurred.")

    def wait_for_element_to_be_clickable(self,locator):
        self.customLogger.debug(msg=
        "Waiting for Element to be clickable with locator: {} ".format(
            locator)
        )

        try:
            element = self.wait.until(EC.element_to_be_clickable( locator))
            self.customLogger.info("Element found clickable")
            return element
        except  exceptions.ElementClickInterceptedException:
            self.customLogger.error(
                "While waiting for element to be clickable - ElementClickInterceptedException Occurred.")

        except exceptions.TimeoutException:
            self.customLogger.error("While waiting for element to be clickable - TimeoutException Occurred.")

    def clear_element(self, element):

        try:
            element.clear()

        except Exception as e:
            self.customLogger.error("While clearing the element exception occurred")
            self.customLogger.error(str(e))

    def send_input(self, element, user_input):
        try:
            element.send_keys(user_input)

        except Exception as e:
            self.customLogger.info("While sending the input to the element an exception occurred.")
            self.customLogger.error(str(e))

    def click_element(self, element):
        try:
            element.click()
        except Exception as e:
            self.customLogger.info("While clicking the element an exception occurred.")
            self.customLogger.error(str(e))

    def wait_until_all_elements_visible(self, locator):
        self.customLogger.debug(msg="Waiting for ALL elements to be visible with locator:{}".format(locator))
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            return elements
        except  exceptions.ElementNotVisibleException:
            self.customLogger.error(
                "While waiting for all elements to be visible - ElementNotVisibleException Occurred.")
        except  exceptions.TimeoutException:
            self.customLogger.error(
                "While waiting for all elements to be visible - TimeoutException Occurred.")

    def wait_until_presence_of_all_elements_located(self, locator):
        self.customLogger.debug("Waiting for all elements to present with locator: {}".format(locator))
        try:
            element = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.customLogger.info("Presence of All Elements Located")
            return element
        except  exceptions.NoSuchElementException:
            self.customLogger.error("While looking for presence of all elements - NoSuchElementException Occurred.")
        except exceptions.TimeoutException:
            self.customLogger.error("While looking for presence of all elements - TimeoutException Occurred.")

    def page_scroll_till_bottom_one_time(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def refresh_page(self):
        self.driver.refresh()

    def wait_for_staleness_of_elements(self, element):
        try:
            element = self.wait.until(EC.staleness_of(element))
            return element
        except exceptions.StaleElementReferenceException:
            self.customLogger.error("Stale Element Reference Exception Occurred.")

    def find_element(self, locator):
        self.customLogger.debug("Finding element with locator:{} ".format(locator))
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))

            return element
        except exceptions.NoSuchElementException:
            self.customLogger.error("NoSuchElementException Occurred.")

    def scroll_till_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView()", element)
            self.customLogger.info("Scrolled till the visibility of the element located")
        except Exception as e:
            self.customLogger.error("Exception Occurred while scrolling till the element")
            self.customLogger.error(str(e))
    def wait_implicitly(self, seconds):
        self.driver.implicitly_wait(seconds)

    def get_attribute_of_element(self, element, attribute):
        try:
            return element.get_attribute(attribute)
        except  exceptions.NoSuchAttributeException:
            self.customLogger.exception("NoSuchAttributeException Occurred.")

    def wait_for_element_to_include_attribute(self, locator, attribute):
        try:
            return self.wait.until(EC.element_attribute_to_include(locator, attribute))
        except  exceptions.NoSuchAttributeException:
            self.customLogger.error("NoSuchAttributeException Occurred.")
