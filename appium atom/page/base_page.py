#-*- coding:utf-8 -*-
#封装方法
from base.base_drive import BaseDriver
class BasePage():
    def __init__(self,driver):
        base_d = BaseDriver()
        self.driver = base_d.android_driver()

    #封装查询方法
    def get_find_element(self,key):
        return self.driver.find_elements_by_class_name(key)
    #在封装一个查询id的方法
    def get_findid_element(self,key):
        return self.driver.find_element_by_id(key)
    
    #封装输入的的方法
    def get_send(self,key,value):
        return self.driver.find_elements_by_class_name(key).send_keys(value)

    #封装click方法
    def find_elemnt_and_click(self,key):
        return self.driver.find_elements_by_class_name(key).click()

    #封装click 查询id的方法
    def find_elemnt_and_idclick(self,key):
        return self.driver.find_elements_by_id(key).click()
    #点击按钮
    def wait_time(self,m):
        return self.driver.implicitly_wait(m)