# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

# 实现8种元素定位
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        elm = self.driver.find_element_by_id('kw')
        elm.send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_name(self):
        elm = self.driver.find_element_by_name('wd')
        elm.send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(1)

    def test_link_txt(self):
        self.driver.find_element_by_link_text('地图').click()
        sleep(1)
    def test_partial_link_text(self):
        self.driver.find_element_by_partial_link_text('加油').click()
        sleep(1)
    def test_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('25ma.cn')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_tag(self):
        input = self.driver.find_element_by_tag_name('input')[0]
        print(input)
        input.send_keys('25ma.cn')
        self.driver.find_element_by_id('su').click()
        sleep(1)

    def test_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('25ma.cn')
        self.driver.find_element_by_id('su').click()
        sleep(1)
    def test_class_name(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('25ma.cn')
        self.driver.find_element_by_id('su').click()
        sleep(1)

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    case = TestCase()
    # 8. 通过class name 查找元素
    # case.test_class_name()
    # 7. 通过css选择器查找元素
    # case.test_css_selector()
    # 6. 通过标签查找元素
    # case.test_tag()
    # 5. 通过xpath 查找元素
    # case.test_xpath()
    # 4. 通过partial_link_text 查找元素
    # case.test_partial_link_text()
    # 3. 通过link_txt查找元素
    # case.test_link_txt()
    # 2. 通过name 查找元素
    # case.test_name()
    # 1. 通过id查找元素
    # case.test_id()

    case.quit()