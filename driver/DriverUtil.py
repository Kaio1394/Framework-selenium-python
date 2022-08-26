from selenium import webdriver


class DriverUtil:
    @staticmethod
    def get_instance():
        return webdriver.Chrome('driver/chromedriver.exe')
