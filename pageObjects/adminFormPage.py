from selenium.webdriver.common.by import By

from base.baseDriver import BaseDriver
from utilities.utils import Logger


class AdminFormPage(BaseDriver):
    customLogger = Logger.sample_logger()
    dropdown_select_xpath = (By.XPATH, "//div[@class='oxd-select-text-input']")
    input_employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")

    input_username = (By.XPATH,
                      "//div[@class='oxd-form-row']//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@class='oxd-input oxd-input--active']")
    button_save = (By.XPATH, "//button[normalize-space()='Save']")
    input_password = (By.XPATH,
                      "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@type='password']")
    input_confirm_password = (By.XPATH,
                              "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@type='password']")
    success_modal = (By.XPATH, "//p[@class= 'oxd-toast oxd-toast--success oxd-toast-container--toast']")
    successfully_saved = (By.XPATH, '//p[text()="Successfully Saved"]')
    success_message = (By.XPATH, '//p[text()="Success"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_role_option(self, role_name):
        locator = (By.XPATH, "//div[@role='listbox']//span[contains(text(),'" + role_name + "')]")
        element = self.wait_for_element_to_be_clickable(locator)
        return element

    def get_status_option(self, status):
        locator = (By.XPATH, "//div[@role='listbox']//span[contains(text(),'" + status + "')]")
        element = self.wait_for_element_to_be_clickable(locator)
        return element

    def tap_selected_status(self, status):

        btn = self.get_status_option(status)
        if btn:
            self.click_element(btn)
            self.customLogger.info("***** Status: " + status + " Clicked *****")
        else:
            self.customLogger.exception(f"***** Unable to click Status: {status} ***** ")

    def tap_selected_role(self, role_name):

            element = self.get_role_option(role_name)
            if element:
                self.click_element(element)
                self.customLogger.info("***** Role: " + role_name + " Clicked *****")
            else:
                self.customLogger.exception(f"***** Unable to click Role: {role_name} ***** ")

    def get_all_selection_elements(self):
        elements = self.wait_until_all_elements_visible(self.dropdown_select_xpath)
        return elements

    def get_role_selection_dropdown(self):

            elements = self.get_all_selection_elements()
            if elements:
                self.customLogger.info(" ***** 0th Selection Element i.e Role dropdown is visible *****")

                return elements[0]
            else:
                self.customLogger.info(" ***** Couldn't get 0th Selection Element i.e Role dropdown *****")

    def get_status_selection_dropdown(self):

            elements = self.get_all_selection_elements()
            if elements:
                self.customLogger.info(" ***** 1st Selection Element i.e Status dropdown is visible *****")
                return elements[1]

            else:
                self.customLogger.info(" ***** Couldn't get 1st Selection Element i.e Status dropdown *****")


    def tap_role_dropdown(self):

        dp = self.get_role_selection_dropdown()
        if dp:
            self.click_element(dp)
            self.customLogger.info("***** Role Dropdown clicked *****")
        else:
            self.customLogger.exception("***** Unable to click Role dropdown *****")


    def tap_status_dropdown(self):

        dp = self.get_status_selection_dropdown()
        if dp:
            self.click_element(dp)
            self.customLogger.info("***** Satus Dropdown Clicked *****")
        else:
            self.customLogger.exception("***** Unable to click status dropdown *****")


    def get_employee_name_input(self):
        element = self.wait_for_element_to_be_visible(self.input_employee_name)
        return element

    def send_employee_name(self, user_name):

        element = self.get_employee_name_input()
        if element:
            self.send_input(element, user_name)
            self.customLogger.info("***** Sent Employee Name *****")
        else:
            self.customLogger.exception(f" ***** Unable to send Employee Name: {user_name} ***** ")


    def get_employee_name_from_dropdown(self, user_name):
        employee_name = (
            By.XPATH, "//div[@class='oxd-autocomplete-wrapper']//span[normalize-space()='" + user_name + "']")
        return self.wait_for_element_to_be_clickable(employee_name)

    def tap_employee_from_dropdown(self, user_name):
        el = self.get_employee_name_from_dropdown(user_name)
        if el:
                self.click_element(el)
                self.customLogger.info("*****Employee: " + user_name + " Clicked *****")
        else:
            self.customLogger.info(f" ***** Unable to click Employee {user_name} ***** ")

    def get_username(self):
        return self.wait_for_element_to_be_visible(self.input_username)

    def send_username(self, user_name):
        self.customLogger.info(f" ***** User Name : {user_name} ***** ")

        element = self.get_username()
        if element:
            self.send_input(element, user_name)
            self.customLogger.info("***** Sent Username *****")
        else:
            self.customLogger.exception(" ***** Unable to send username ***** ")


    def get_password(self):
        return self.wait_for_element_to_be_visible(self.input_password)

    def send_password(self, password):
        self.customLogger.info(password)
        element = self.get_password()
        if element:
            self.send_input(element, password)
            self.customLogger.info("***** Sent Password *****")
        else:
            self.customLogger.exception(" ***** Unable to send Password ***** ")


    def get_confirm_password(self):
        return self.wait_for_element_to_be_visible(self.input_confirm_password)

    def send_confirm_password(self, password):
        self.customLogger.debug(f"***** Confirm Password : {password} *****")
        element = self.get_confirm_password()
        if element:
                self.send_input(element, password)
                self.customLogger.info("***** Sent Confirm Password *****")
        else:
                self.customLogger.exception(" ***** While sending confirm password an Exception occurred ***** ")

    def get_save_button(self):
        return self.wait_for_element_to_be_clickable(self.button_save)

    def click_save_button(self):
            el = self.get_save_button()
            if el:
                self.click_element(el)
                self.customLogger.info("***** Save Button Clicked *****")
            else:
                self.customLogger.exception("***** Save Button could not be clicked. *****")

    def get_success_modal(self):
        return self.wait_for_element_to_be_visible(self.success_modal)

    def get_success_message(self):
        return self.wait_for_element_to_be_visible(self.success_message)

    def get_successfully_saved_message(self):
        return self.wait_for_element_to_be_visible(self.successfully_saved)
