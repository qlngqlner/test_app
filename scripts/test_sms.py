import sys, os
sys.path.append(os.getcwd())

from Page.Page import Page
from Base.get_driver import get_driver
import pytest

class Test_Sms:

    def setup_class(self):
        self.page_obj = Page(get_driver())

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.fixture(scope ="class",autouse=True)

    def in_sms_page(self):
        self.page_obj.get_sms_page().add_sms()

        self.page_obj.get_sms_page().add_phone("18310787064")

    @pytest.mark.parametrize("send_ms",["hi","你好","嘿嘿"])

    def test_send_sms(self,send_ms):

        send_result =self.page_obj.get_sms_page().send_sms(send_ms)

        assert send_ms in send_result