#-*-coding: utf-8-*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import send_recv_mail
class AtomLive():
    #打开app
    def star(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "3458553639393498"#"127.0.0.1:21503"
        caps["appPackage"] = "com.atom.cam"
        caps["appActivity"] = "com.hualai.cam.home.SmartHomeMainActivity"
        caps["automationName"] = "uiautomator2"
        #com.atom.cam/com.hualai.cam.home.SmartHomeMainActivity
        #com.atom.cam/com.hualai.cam.home.SmartHomeMainActivity
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyboard"] = True
        caps['noReset'] = True # true:不重新安装APP，false:重新安装app   
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)
    #登录
    def login(self):
        #输入账号
        el1 = self.driver.find_elements_by_class_name("android.widget.EditText")[0]       
        el1.click()
        el1.send_keys("ouqingwei@hualaikeji.com")
        #输入密码
        #el2 = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'com.atom.cam:id/login_input_et')])")
        #el2 = self.driver.find_element_by_class_name("android.widget.EditText[@index='1']")
        el2 = self.driver.find_elements_by_class_name("android.widget.EditText")[1]
        el2.click()
        el2.send_keys("00000000")
        #点击登录按钮
        el3 = self.driver.find_element_by_id("com.atom.cam:id/login_btn_login")
        el3.click()
        self.driver.implicitly_wait(15)
        #需要获取验证码？

    #进入直播
    def get_live(self):
        count = 10
        while count:
            el1 = self.driver.find_element_by_id("com.atom.cam:id/wyze_all_device_list_camera_iv_iconass")
            el1.click()
            self.driver.implicitly_wait(10)
            #点击返回按钮，返回设备列表页
            el2 = self.driver.find_element_by_id("com.atom.cam:id/iv_back")
            el2.click()
            self.driver.implicitly_wait(2)
            #需要加一个判断，判断固件自动重启，通过break终止循环？并且输出在第几次的时候产生了重启

    # def get_mail_code(self):
    #     host = "imap.qiye.163.com"  # "imap.126.com"
    #     username = "ouqingwei@hualaikeji.com"  # 用户名
    #     password = "00000000"  # 密码
    #     sender = "no-reply@support.atomtech.co.jp"
    #     keyword = "認証コード："
    #     code = send_recv_mail.getMailCaptcha(host, username, password, sender=sender, keyword=keyword)
    #     print code
            
    
if __name__ == "__main__":
    atom = AtomLive()
    atom.star()
    atom.login()
    atom.get_live()
