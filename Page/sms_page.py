from Base.Base import Base
import Page

class Sms_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def add_sms(self):
        # 点击添加短信按钮
        self.click_element(Page.sms_add_btn)

    def add_phone(self, phone):
        # 输入手机号
        self.input_element(Page.sms_recip_phone, phone)

    def send_sms(self, send_text):
        # 发送短信
        self.input_element(Page.sms_send_text, send_text)
        # 点击发送按钮
        self.click_element(Page.sms_send_btn)
        # 获取结果列表
        result_sms = self.search_elements(Page.sms_get_send_text, timeout=5)

        return [i.text for i in result_sms]