from selenium.webdriver.common.by import By

from pages.Helper import Helper

LOCATOR_SEARCH_BY_NAME = "q"
LOCATOR_CLICK_SEARCH = "//div[@*='FPdoLc lJ9FBc']/center/*[@*='Pesquisa Google']"

class Google_page:
    def __init__(self):
        self.driver = Helper()

    def search_in_google(self, value):
        self.driver.send_keys(By.NAME, LOCATOR_SEARCH_BY_NAME, value)

    def close_window(self):
        self.driver.close()

    def click_search(self):
        self.driver.send_click(By.XPATH, LOCATOR_CLICK_SEARCH)

    def navigate_home_page(self):
        self.driver.get_url("https://google.com")

    def return_url_google_home(self):
        return self.driver.get_url_browser()