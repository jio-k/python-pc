#-*- coding:utf-8 -*-
from appium import webdriver
class BaseDriver():
    def android_driver(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:21503"
        caps["appPackage"] = "com.atom.cam"
        caps["appActivity"] = "com.hualai.cam.home.user.activity.LogInActivity"
        caps["automationName"] = "uiautomator2" #automationName版本
        caps["autoGrantPermissions"] = "true" #有需要获取权限的弹窗默认点击确定
        caps["unicodeKeyboard"] = True 
        caps["noReset"] = True # true:不重新安装APP，false:重新安装app

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(10)
        return self.driver

    def quit(self):
        self.driver.quit()