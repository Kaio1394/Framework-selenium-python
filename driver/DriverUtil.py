from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DriverUtil:
    @staticmethod
    def get_instance():
        return webdriver.Chrome(ChromeDriverManager().install())
