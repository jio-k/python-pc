#-*- coding:utf-8 -*-
from base.base_drive import BaseDriver
from page.base_page import BasePage
class AtomCase():
    #执行打开app的方法
    def setup(self):
        self.base_d = BaseDriver().android_driver()
    
    #登录
    def login_case(self):
        self.b = BasePage()
        #找到账号、输入账号
        self.b.find_elemnt_and_click("android.widget.EditText"[0])
        self.b.get_send("android.widget.EditText"[0],"ouqingwei@hualaikeji.com")
        #找到密码、输入密码
        self.b.find_elemnt_and_click("android.widget.EditText")[1]
        self.b.get_send("android.widget.EditText"[1],"00000000")

        #登录
        self.b.find_elemnt_and_click("com.atom.cam:id/login_btn_login")
        #判断登录之后能查询到一些文字或者其他信息assert

    #进入实时浏览、返回
    def live_case(self):
        count = 20
        while count:
            self.b.find_elemnt_and_idclick("com.atom.cam:id/wyze_all_device_list_camera_iv_iconass")
            self.b.wait_time(15)
            #点击返回按钮，返回设备列表页
            self.b.find_elemnt_and_idclick("com.atom.cam:id/iv_back")
            self.b.wait_time(5)
            #需要加一个判断，判断固件自动重启，通过break终止循环？并且输出在第几次的时候产生了重启



    #返回设备列表


    #执行最后执行完后关闭app的方法
    def teardown(self):
        self.base_d.quit()