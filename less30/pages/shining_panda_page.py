from less30.pages.base_page import BasePage
from less30.locators.shining_panda_page_loc import ShiningPandaLoc


class ShiningPandaPage(BasePage):

    def verify_shining_panda_url(self):
        shining_panda_url = self.chrome.current_url
        assert shining_panda_url == ShiningPandaLoc.shining_panda_url_loc, \
            'Error, Shining Panda page URL is not equall recieved link!'
