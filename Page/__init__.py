from selenium.webdriver.common.by import By

# 搜索按钮
search_btn = (By.ID, "com.android.settings:id/search")
# 输入框
search_input = (By.ID, "android:id/search_src_text")
# 结果列表
search_result = (By.ID, "com.android.settings:id/title")

"""
    发送短信
"""
# 新增短信按钮
sms_add_btn = (By.ID, "com.android.mms:id/action_compose_new")
# 接收短信用户
sms_recip_phone = (By.ID, "com.android.mms:id/recipients_editor")
# 发送信息输入框
sms_send_text = (By.ID, "com.android.mms:id/embedded_text_editor")
# 发送短信按钮
sms_send_btn = (By.ID, "com.android.mms:id/send_button_sms")
# 获取已发送内容
sms_get_send_text = (By.ID, "com.android.mms:id/text_view")