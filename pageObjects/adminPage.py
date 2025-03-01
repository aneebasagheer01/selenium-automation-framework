from selenium.webdriver.common.by import By
from base.baseDriver import BaseDriver
from pageObjects.adminFormPage import AdminFormPage
from utilities.utils import Logger


class AdminPage(BaseDriver):
    customLogger = Logger.sample_logger()
    button_add_xpath = (By.XPATH, "//button[normalize-space()='Add']")
    input_box_select_xpath = (By.XPATH, "//div[@class='oxd-select-text-input']")
    button_search_xpath = (By.XPATH, "//button[normalize-space()='Search']")
    all_role_rows = (By.XPATH, "//div[@class='oxd-table-card']//div[@role='row']//div[@role='cell'][3]")
    all_username_rose = (By.XPATH, "//div[@class='oxd-table-card']//div[@role='row']//div[@role='cell'][2]")
    search_box_username_xpath = (By.XPATH,
                                 "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@class='oxd-input oxd-input--active']")

    text_info_xpath = (By.XPATH, '//*[@id="oxd-toaster_1"]//p[normalize-space()="Info"]')
    text_no_records_found = (By.XPATH, '//*[@id="oxd-toaster_1"]//p[normalize-space()="No Records Found"]')
    all_rows = (By.XPATH, '//div[@role="row"]')
    table_body = (By.XPATH, "//div[@class='oxd-table-body']")
    visible_no_records_found = (
        By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[.='No Records Found']")

    row_status_xpath = (By.XPATH, "//div[@class='oxd-table-card']//div[@role='row']//div[@role='cell'][5]")

    heading_system_user_xpath = (By.XPATH, "//h5[normalize-space()='System Users']")

    input_employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    reset_button = (By.XPATH, "//button[normalize-space()='Reset']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_table_body(self):

            el = self.wait_for_element_to_be_visible(self.table_body)
            if el:
                self.customLogger.info(" ***** Table Body is Visible Now *****")
                return el
            else:
                self.customLogger.error(" ***** Table Body was found Not Visible ***** ")

    def get_employee_name_input(self):
        el = self.wait_for_element_to_be_visible(self.input_employee_name)
        return el

    def get_reset_button(self):
        el = self.wait_for_element_to_be_clickable(self.reset_button)
        return el

    def send_employee_name(self, employee_name):

            e_name = self.get_employee_name_input()
            if e_name:
                self.send_input(e_name, employee_name)
                self.customLogger.info("***** Sent Employee Name *****")
            else:
                self.customLogger.error("***** Unable to Sent Employee Name *****")

    def click_reset_button(self):

            el = self.get_reset_button()
            if el:
                self.click_element(el)
                self.customLogger.info("***** Reset Button Clicked *****")
            else:
                self.customLogger.error("***** Unable to click Reset Button *****")

    def get_username_searchbox(self):
        element = self.wait_for_element_to_be_visible(self.search_box_username_xpath)
        return element

    def get_add_button(self):
        element_found = self.wait_for_element_to_be_clickable(self.button_add_xpath)
        return element_found

    def get_role_option(self, role):
        locator = (By.XPATH, "//div[@class='oxd-select-option'][@role='option'][normalize-space()='" + role + "']")
        element = self.wait_for_element_to_be_clickable(locator)
        return element

    def get_search_button(self):
        element = self.wait_for_element_to_be_clickable(self.button_search_xpath)
        return element

    def get_all_selection_elements(self):
        element = self.wait_until_all_elements_visible(self.input_box_select_xpath)
        return element

    def click_add_button(self):

            element = self.get_add_button()
            if element:
                self.click_element(element)
                self.customLogger.info("***** Add Button Clicked *****")
                page = AdminFormPage(self.driver)
                return page
            else:
                self.customLogger.error("***** Unable to click Add Button *****")

    def get_role_selection_box(self):
            element = self.get_all_selection_elements()
            if element:
                self.customLogger.info(" ***** Role Selection Element is Visible *****  ")
                return element[0]
            else:
                self.customLogger.error(" ***** Role Selection Element is not Visible ***** ")

    def get_status_selection_box(self):

            element = self.get_all_selection_elements()

            if element:
                self.customLogger.info(" ***** Status Selection Element is Visible *****  ")
                return element[1]
            else:
                self.customLogger.error(" ***** Status Selection Element is not Visible ***** ")


    def tap_role_selection_box(self):

        element = self.get_role_selection_box()
        if element:
            self.click_element(element)
            self.customLogger.info("***** Role Drop Down Clicked *****")
        else:
            self.customLogger.error("***** Unable to click Role Drop Down Clicked *****")

    def tap_status_selection_box(self):
        element = self.get_status_selection_box()
        self.click_element(element)

    def tap_role(self, role):
        element = self.get_role_option(role)
        if element:
            self.click_element(element)
            self.customLogger.info("***** Role: " + role + " Option Clicked *****")
        else:
            self.customLogger.error("***** Unable to click Role: " + role + " Option *****")

    def tap_search(self):
        button = self.get_search_button()
        if button:
            self.click_element(button)
            self.customLogger.info("***** Search Button Clicked *****")
        else:
            self.customLogger.error("***** Unable to click Search Button *****")
    def get_all_role_cells(self):
        elements = self.wait_until_presence_of_all_elements_located(self.all_role_rows)
        return elements

    def send_user_name(self, user_name):
        element = self.get_username_searchbox()
        if element:
            self.send_input(element, user_name)
            self.customLogger.info("***** Sent User Name *****")
        else:
            self.customLogger.error("***** Unable to send username *****")
    def get_all_username_rows(self):
        elements = self.wait_until_presence_of_all_elements_located(self.all_username_rose)
        return elements

    def staleness_of_rows(self):
        self.wait_for_staleness_of_elements(self.driver.find_element(By.XPATH, "//div[@class='oxd-table-body']"))

    def get_disappearing_info_element(self):
        return self.wait_for_element_to_be_visible(self.text_info_xpath)

    def get_disappearing_no_records_found_elements(self):
        return self.wait_for_element_to_be_visible(self.text_no_records_found)

    def get_visible_error_info(self):
        return self.wait_for_element_to_be_visible(self.visible_no_records_found)

    def get_enabled_option(self):
        return self.wait_for_element_to_be_clickable(self.option_Enabled_xpath)

    def get_disabled_option(self):
        return self.wait_for_element_to_be_clickable(self.option_Disabled_xpath)

    def get_selected_status(self, status):
        option = (By.XPATH, '//div[@role="option"]/span[normalize-space()="' + status + '"]')
        el = self.wait_for_element_to_be_clickable(option)
        return el

    def tap_selected_status(self, status):

        el = self.get_selected_status(status)
        if el:
            self.click_element(el)
            self.customLogger.info("*****Status: " + status + " Option Clicked *****")
        else:
            self.customLogger.error("***** Unable to click Status: " + status + " Option *****")
    def get_status_rows(self):
        element = self.wait_until_presence_of_all_elements_located(self.row_status_xpath)
        return element

    def get_first_row_username(self):
        locator = (By.XPATH, "//div[@class='oxd-table-card'][1]//div[@class='oxd-table-cell oxd-padding-cell'][2]")
        return self.wait_for_element_to_be_visible(locator)

    def wait_until_system_users_heading(self):
        self.wait_for_element_to_be_visible(self.heading_system_user_xpath)
