#!/usr/bin/python3
# _*_ coding:utf-8_*_
"""
模拟爬虫
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import xlrd
from time import sleep


def main():
    print('[!]Starting...')
    driver = webdriver.Chrome()
    data = xlrd.open_workbook('InputTest1.xlsx')
    table = data.sheet_by_index(0)
    A1 = table.cell(1, 0).value
    B1 = table.cell(1, 1).value
    driver.set_page_load_timeout(20)
    try:
        driver.get("http://www.bigschedules.com/")
    except Exception as e:
        pass
    driver.find_element_by_id("main_feature_beta_span_close").click()
    driver.find_element_by_id("targetOriginal").clear()
    driver.find_element_by_id("targetOriginal").send_keys(A1)
    driver.find_element_by_id("targetOriginal").send_keys(Keys.ENTER)
    driver.find_element_by_id("targetDestination").clear()
    driver.find_element_by_id("targetDestination").send_keys(B1)
    driver.find_element_by_id("targetDestination").send_keys(Keys.ENTER)
    driver.find_element_by_id("main_a_search").click()


    sleep()







if __name__=='__main__':
    print('123')
    main()