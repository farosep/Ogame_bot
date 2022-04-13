#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import Decider
import InfoScrapper
from Login import Login
import datetime
from data import Data




class StartGame:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.data = Data(self.driver)
        self.driver.implicitly_wait(3)


    def start(self):
        Login(self.driver, self.data)
        print(f'Залогинились успешно: time ({datetime.datetime.now().strftime("%H:%M:%S")})')
        while True:
            #  собираем информацию
            InfoScrapper.get_all_info(self.driver, self.data)
            Decider.decide_what_to_do(self.data)


a = StartGame()
a.start()
