from selenium import webdriver
import pytest

from less30.pages.shining_panda_page import ShiningPandaPage


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome(r'C:\Users\Admin\PycharmProjects\pythonProject\selenium_test\chromedriver.exe')


def test_go_to_shining_panda_page(open_browser):
    link = 'https://plugins.jenkins.io/shiningpanda/'
    shining_panda_page = ShiningPandaPage(browser, link)
    try:
        shining_panda_page.open_site()
        shining_panda_page.verify_shining_panda_url()
    finally:
        browser.quit()
