#!/usr/bin/env python
# encoding: utf-8


"""
@version: python27
@author: fafa
@site: http://www.phpgao.com
@software: PyCharm Community Edition
@file: createpeplecon.py
@time: 2016/12/17 0017 下午 4:33
获取系统版本：adb shell getprop ro.build.version.release
# 5.1.1
获取系统api版本：adb shell getprop ro.build.version.sdk
# sdk:22
"""
from appium import webdriver
import time


def test_createpeplecon():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['deviceName'] = '15983806'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    print 'sss'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print 'ss'
    y = driver.find_element_by_class_name('android.widget.Button')
    y.click()
    time.sleep(1)
    user = driver.find_element_by_name(u'姓名')
    user.click()
    user.send_keys(u'发发')
    y = driver.find_element_by_name(u'公司')
    y.click()
    y.send_keys(u'深圳南山科技')

    z = driver.find_element_by_name(u'职位')
    z.click()
    z.send_keys(u'软件测试')

    phone = driver.find_element_by_name(u'电话')
    phone.click()
    phone.send_keys('123456')
    driver.save_screenshot('tny.png')
    driver.find_element_by_id('com.android.contacts:id/ok').click()
    driver.quit()


test_createpeplecon()
