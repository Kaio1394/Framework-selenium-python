from pages.Helper import Helper

LOCATOR_SEARCH_BY_NAME = "q"
LOCATOR_CLICK_SEARCH = "//div[@*='FPdoLc lJ9FBc']/center/*[@*='Pesquisa Google']"
LOCATOR_SEARCH_LOADING = "//input[@aria-label='Pesquisar']"

class Google_page:
    def __init__(self):
        self.driver = Helper()

    def search_in_google(self, value):
        self.driver.send_keys('name', LOCATOR_SEARCH_BY_NAME, value)

    def close_window(self):
        self.driver.close()

    def click_search(self):
        self.driver.send_click('xpath', LOCATOR_CLICK_SEARCH)

    def navigate_home_page(self):
        self.driver.get_url("https://google.com")

    def return_url_google_home(self):
        return self.driver.get_url_browser()

    def url_contains_search(self, value) -> bool:
        url = self.return_url_google_home().lower()
        if str(value).lower() in url:
            return True
        else:
            return False

    def wait_until_loading_page_search(self):
        self.driver.wait_until(5, 'XPATH', LOCATOR_SEARCH_LOADING)