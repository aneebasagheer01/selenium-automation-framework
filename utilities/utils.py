import inspect
import logging
import softest
import csv
from faker import Faker


class Logger:
    @staticmethod
    def sample_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        ch = logging.FileHandler("../logs/automation.logs")

        formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s - %(levelname)s : %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p")
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger


class Utilities(softest.TestCase):
    Faker = Faker()

    def assert_all_items(self, actual_list, expected_value):

        try:
            for element in actual_list:
                self.soft_assert(self.assertEqual, element.text, expected_value)
            self.assert_all()
        except Exception as e:
            print("Assertions error: ",e)
            raise e

    @staticmethod
    def read_data_from_csv(user_file_name):
        data_list = []
        file_handler = open(file=user_file_name, mode='r')
        reader = csv.reader(file_handler)
        next(reader)
        for row in reader:
            data_list.append(row)
        return data_list

    def assert_element_visible(self, element):
        self.soft_assert(self.assertTrue, element)

    def assert_all_assertions(self):
        try:
            self.assert_all()
        except Exception as e:
            print("Assertions error: ",e)
            raise e

    def assert_attributes(self, actual_attribute_value, expected_value):
        self.soft_assert(self.assertEqual, actual_attribute_value, expected_value)

    def generate_random_user_name(self):
        name = self.Faker.user_name()
        return name

    def generate_random_password(self):
        password = self.Faker.password(length=7, lower_case=True, upper_case=True, special_chars=True, digits=True)
        return password


