import unittest
from dir_massa import GetMassa
from pages.Pages import Pages


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Pages()
        self.driver.get_google_page.navigate_home_page()
        self.driver.get_google_page.wait_until_loading_page_search()

    def tearDown(self) -> None:
        self.driver.get_google_page.close_window()

    def teste01_valid_home_page(self):
        self.assertEqual(self.driver.get_google_page.return_url_google_home(),
                         GetMassa.return_massa('url_google'))

    def test02_search(self):
        self.teste01_valid_home_page()
        search_atletico = 'Atletico mg'
        self.driver.get_google_page.search_in_google(search_atletico)
        self.driver.get_google_page.click_search()
        self.assertTrue(self.driver.get_google_page.url_contains_search(search_atletico.replace(' ', '+')))


