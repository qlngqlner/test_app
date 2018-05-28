from Page.search_page import Search_Page
from Page.sms_page import Sms_Page
"""
    统一入口类
"""

class Page:
    def __init__(self, driver):
        self.driver = driver

    # 返回搜索页面对象
    def get_search_page(self):
        return Search_Page(self.driver)

    # 返回短信页面对象
    def get_sms_page(self):
        return Sms_Page(self.driver)
