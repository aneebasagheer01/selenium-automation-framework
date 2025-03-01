from selenium.webdriver.common.by import By
from base.baseDriver import BaseDriver
from pageObjects.adminPage import AdminPage
from utilities.utils import Logger


class DashboardPage(BaseDriver):
    customLogger = Logger.sample_logger()
    link_admin_xpath = (By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']/span[normalize-space()='Admin']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_admin_side_menu(self):
        element = self.wait_for_element_to_be_clickable(self.link_admin_xpath)
        return element

    def click_admin_side_menu(self):
        element = self.get_admin_side_menu()
        if element:
            self.click_element(element)
            self.customLogger.info("***** Admin Side Menu Clicked *****")
            admin_page = AdminPage(self.driver)
            return admin_page
        else:
            self.customLogger.error("***** Unable to click Admin Side Menu")