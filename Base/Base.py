from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver):
        self.driver = driver


    def search_element(self, loc,timeout):

        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc,timeout):

         return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(*loc))

    def click_element(self,loc, timeout=5):

        self.search_element(loc, timeout).click()

    def input_element(self,loc, text,timeout=5):

        # 定位到元素
        input_text = self.search_element(loc, timeout)
        input_text.clear()
        input_text.send_keys(text)
