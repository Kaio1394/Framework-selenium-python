from selenium import webdriver
from selenium.webdriver.common.by import By

from driver.DriverUtil import DriverUtil


class Helper:
    def __init__(self):
        self.driver = DriverUtil.get_instance()

    def get_url(self, value):
        self.driver.get(value)

    def send_keys(self, by, by_value, value):
        self.driver.find_element(by, by_value).send_keys(value)

    def send_click(self, by, by_value):
        self.driver.find_element(by, by_value).click()

    def close(self):
        self.driver.close()
