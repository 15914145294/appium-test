# -*- coding: utf-8 -*-
import sys
import os
import unittest
import traceback
from time import sleep
from uiHelper import UiHelper


class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        uiHelper = UiHelper("deviceConfig.txt")
        uiHelper.initDriver()
        try:
            # 查找创建新联系人按钮
            createContactButton = None
            try:
                # 如果手机没有联系人，则通过create_contact_button来创建。 此处通过控件id来查找
                createContactButton = uiHelper.findElement("com.android.contacts:id/create_contact_button")
            except:
                # 如果手机已经有其他联系人,则通过底部的添加联系人菜单来添加
                createContactButton = uiHelper.findElement("com.android.contacts:id/menu_add_contact")
            # 点击创建按钮
            createContactButton.click()

            # 请注意此处代码与另外一个helloworld示例的差别
            try:
                # 等待'本地保存'按钮显示,如果等待5秒还没有显示,就会抛出异常,但是该异常会被捕获,不影响后续测试
                uiHelper.waitForElementBySystem("com.android.contacts:id/left_button", 5)
                # 如果能执行到这里,说明找到了该按钮,则点击它
                uiHelper.clickElement("com.android.contacts:id/left_button")
            except:
                pass

            # 点击姓名，并输入。此处是通过控件的文本来找到
            name = uiHelper.findElement(u"姓名")
            name.click()
            name.send_keys(u"冒烟测试")
            # 点击电话输入框，并输入。注意此处是通过找到一组控件，并操作第n个控件，n从0开始。
            telephoneControls = uiHelper.findElements(u"电话")
            telephoneControls[1].click()
            telephoneControls[1].send_keys("01012345678")
            # 保存一个屏幕截图
            uiHelper.saveScreenshot("afterinput.png")
            # 点击完成按钮
            completeButton = uiHelper.findElement("com.android.contacts:id/icon")
            completeButton.click()
            # 等待联系人详情页面显示，请注意此处代码与另外一个helloworld示例的差别
            uiHelper.waitForElement("com.android.contacts/.activities.ContactDetailActivity", 10)
            # 验证联系的信息是否与输入一样
            barTitle = uiHelper.findElement("android:id/action_bar_title")
            self.assertEqual(barTitle.text, u"冒烟测试")
            contactDatas = uiHelper.findElements("com.android.contacts:id/data")
            self.assertEqual(contactDatas[0].text, "010 1234 5678")
            # 最后保存一个截图用于人工查看
            uiHelper.saveScreenshot("newContact.png")
        finally:
            if (uiHelper != None):
                uiHelper.quitDriver()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)
