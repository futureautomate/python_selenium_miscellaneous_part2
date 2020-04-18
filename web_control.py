# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:08:54 2020

@author: Tejas
"""

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('driver path', options=options)
time.sleep(3)

driver.get('http://google.com')

driver.get('http://facebook.com')

driver.back()

driver.forward()

driver.refresh()

driver.execute_script("window.open('')")
driver.switch_to_window(driver.window_handles[1])

driver.get('http://google.com')
driver.switch_to_window(driver.window_handles[0])
driver.title

driver.close()
