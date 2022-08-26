import unittest

from pages.Pages import Pages
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Pages()
        self.driver.get_google_page.navigate_home_page()
        # self.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")

    def tearDown(self) -> None:
        self.driver.get_google_page.close_window()

    def test_search_google(self):
        self.assertEqual(self.driver.get_google_page.return_url_google_home(), "https://www.google.com/")  # add assertion here


if __name__ == '__main__':
    unittest.main()
