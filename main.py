from dir_massa import GetMassa
from pages.Pages import Pages
import time

if __name__ == '__main__':
    pages = Pages()
    pages.get_google_page.navigate_home_page()
    pages.get_google_page.search_in_google(GetMassa.return_massa('search'))
    time.sleep(2)
    pages.get_google_page.click_search()
    pages.get_google_page.close_window()

