import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

class Config:

    @staticmethod
    def get_url():
        return config.get("COMMON", "base_url")

    @staticmethod
    def get_browser():
        return config.get("COMMON", "browser")

    @staticmethod
    def time_out():
        return config.get("COMMON", "time_out")

    @staticmethod
    def get_username():
        return config.get("LOGIN", "username")

    @staticmethod
    def get_password():
        return config.get("LOGIN", "password")