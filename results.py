#!/Demi/python
import  sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,os
import xlrd


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.bigschedules.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_1(self):
        data = xlrd.open_workbook("InputTest1.xlsx")
        table = data.sheets()[0]
        table = data.sheet_by_index(0)
        cell_A1 = table.cell(1,0).value
        cell_B2 = table.cell(1,1).value
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("main_feature_beta_span_close").click()
        driver.find_element_by_id("targetOriginal").clear()
        driver.find_element_by_id("targetOriginal").send_keys(cell_A1)
        time.sleep(2)
        driver.find_element_by_id("targetOriginal").send_keys(Keys.ENTER)
        driver.find_element_by_id("targetDestination").clear()
        driver.find_element_by_id("targetDestination").send_keys(cell_B2)
        time.sleep(2)
        driver.find_element_by_id("targetDestination").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("main_a_search").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except Exception, e:
            print e
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

if __name__ == "__main__":
    unittest.main()

