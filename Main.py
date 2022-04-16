#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import Decider
import InfoScrapper
from Login import Login
import datetime
from data import Main_data, Colony, Colony_data
from selenium.webdriver.common.by import By


class StartGame:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.main_data = Main_data(self.driver)
        self.driver.implicitly_wait(3)
        self.login = Login(self.driver, self.main_data)

    def start(self):
        self.login.get_in_account()
        print(f'Залогинились успешно: time ({datetime.datetime.now().strftime("%H:%M:%S")})')
        self.get_colonies(self.main_data)
        while True:
            for i in self.main_data.Colonies:
                #  собираем информацию
                InfoScrapper.get_all_info(self.driver, self.main_data, self.main_data.Colonies[i].colony_data)
                Decider.decide_what_to_do(self.main_data, self.main_data.Colonies[i].colony_data)
            if self.driver.current_url == 'https://lobby.ogame.gameforge.com/ru_RU/hub':
                self.login.get_in_server()

    def get_colonies(self, main_data):
        a = self.driver.find_elements(By.XPATH, '//*[@id="planetList"]//child::div')
        for i in range(len(a)):
            main_data.Colonies[f'Colony{i + 1}'] = Colony(self.driver, Colony_data(self.driver))
            main_data.Colonies[f'Colony{i + 1}'].ref = f'//*[@id="planetList"]//child::div[{i + 1}]'

a = StartGame()
a.start()
