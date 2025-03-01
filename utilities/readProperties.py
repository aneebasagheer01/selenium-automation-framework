import configparser

parser = configparser.RawConfigParser()
parser.read("../configurationFiles/common.ini")


class readConfig:
    @staticmethod
    def get_base_url():
        base_url = parser.get("common info", "base_url")
        return base_url

    @staticmethod
    def get_user_name():
        user_name = parser.get("common info", "user_name")
        return user_name

    @staticmethod
    def get_password():
        password = parser.get("common info", "password")
        return password
