from Base.Base import Base
import Page

class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_searchx(self):
        # 点击搜索按钮
        self.click_element(Page.search_btn)


    def search_text(self,text_value):
        # 完成搜索
        # 输入内容
        self.input_element(Page.search_input,text_value)
        # 获取结果列表
        result = self.search_elements(Page.search_result, timeout=5)
        return [i.text for i in result]