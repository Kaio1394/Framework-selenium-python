from selenium import webdriver


class DriverUtil:
    @staticmethod
    def get_instance():
        return webdriver.Chrome('C:/Users/Usuario/Documents/python/Framework-selenium-python/driver/chromedriver.exe')
