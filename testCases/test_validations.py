import pytest
import softest
from utilities.utils import Utilities
from ddt import data, ddt, unpack


@pytest.mark.usefixtures("setup_and_teardown_cls")
@ddt
class Test_001(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self,request):

        self.ut = Utilities()
        systems_user_url="https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        test_name = request.node.name
        self.customLogger.info(f" =========== {test_name} Started ==========  ")
        url=self.home.get_current_url()
        if url==systems_user_url:
            pass
        else:
            self.home.open_url(systems_user_url)
        self.home.refresh_page()
        yield

        self.customLogger.info(f" =========== {test_name} Ended ==========  ")
    @data(*Utilities.read_data_from_csv("../testData/role_filter_data.csv"))
    @unpack
    def test_role_filter(self, user_role):
        self.admin.tap_role_selection_box()
        self.admin.tap_role(user_role)
        self.admin.tap_search()
        self.admin.get_table_body()
        self.admin.page_scroll_till_bottom_one_time()
        roles = self.admin.get_all_role_cells()
        self.ut.assert_all_items(roles, user_role)

    @data(*Utilities.read_data_from_csv("../testData/role_username_filter_valid_data.csv"))
    @unpack
    def test_search_by_role_and_username_valid(self, user_role, username):
        self.admin.send_user_name(username)
        self.admin.tap_role_selection_box()
        self.admin.tap_role(user_role)
        self.admin.tap_search()
        self.admin.get_table_body()
        self.admin.page_scroll_till_bottom_one_time()
        roles = self.admin.get_all_role_cells()
        self.ut.assert_all_items(roles, user_role)
        user_names = self.admin.get_all_username_rows()
        self.ut.assert_all_items(user_names, username)


    @data(*Utilities.read_data_from_csv("../testData/role_username_filter_invalid_data.csv"))
    @unpack
    def test_search_by_role_and_username_invalid(self, role, username):
        self.admin.send_user_name(username)
        self.admin.tap_role_selection_box()
        self.admin.tap_role(role)
        self.admin.tap_search()
        self.admin.get_table_body()
        info = self.admin.get_disappearing_info_element()
        no_records_found = self.admin.get_disappearing_no_records_found_elements()
        self.ut.assert_element_visible(info)
        self.ut.assert_element_visible(no_records_found)
        visible_error = self.admin.get_visible_error_info()
        self.ut.assert_element_visible(visible_error)
        self.ut.assert_all_assertions()
        

    @data(*Utilities.read_data_from_csv("../testData/role_status_filter_data_valid.csv"))
    @unpack
    def test_by_role_and_status_filter_valid(self, role, status):
        self.admin.tap_role_selection_box()
        self.admin.tap_role(role)
        self.admin.tap_status_selection_box()
        self.admin.tap_selected_status(status)
        self.admin.tap_search()
        self.admin.get_table_body()
        self.admin.page_scroll_till_bottom_one_time()
        actual_status = self.admin.get_status_rows()
        self.ut.assert_all_items(actual_status, status)
        actual_role = self.admin.get_all_role_cells()
        self.ut.assert_all_items(actual_role, role)
        self.ut.assert_all_assertions()

    @data(*Utilities.read_data_from_csv('../testData/user_role.csv'))
    @unpack
    def test_add_user(self, role, status, employee_name, employee_option):
        admin_form = self.admin.click_add_button()
        user_pass = self.ut.generate_random_password()
        user_name = self.ut.generate_random_user_name()

        admin_form.tap_role_dropdown()
        admin_form.tap_selected_role(role)
        admin_form.tap_status_dropdown()
        admin_form.tap_selected_status(status)
        admin_form.send_employee_name(employee_name)
        admin_form.tap_employee_from_dropdown(employee_option)
        admin_form.send_username(user_name)
        self.admin.page_scroll_till_bottom_one_time()
        admin_form.send_password(user_pass)
        admin_form.send_confirm_password(user_pass)
        admin_form.click_save_button()
        el = admin_form.get_successfully_saved_message()
        el2 = admin_form.get_success_message()
        self.ut.assert_element_visible(el)
        self.ut.assert_element_visible(el2)
        self.admin.wait_until_system_users_heading()
        self.ut.assert_all_assertions()



