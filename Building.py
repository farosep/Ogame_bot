#! /usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import Fore, Style
from selenium.webdriver.common.by import By
import datetime


class Building:
    def __init__(self, driver, data):
        self.data = data
        self.driver = driver
        self.ref_to_upgrade_button = ''
        self.level_ref = ''
        self.blocked_level_ref = ''
        self.level = 0
        self.name = ''
        self.available_to_upgrade = False
        self.page = 'https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies'

    def try_to_upgrade(self):
        if self.available_to_upgrade:
            try:
                self.driver.get(self.page)
                self.driver.find_element(By.CSS_SELECTOR, self.ref_to_upgrade_button).click()
                print(Fore.BLUE + f'{self.name} mine was built')
                print(Style.RESET_ALL)
                return True
            except:
                print(Fore.RED + f'{self.name} Mine was NOT built')
                print(Style.RESET_ALL)
            return False

    def get_info(self):
        self.get_level()
        self.get_available()

    def get_level(self):
        try:
            self.level = int(self.driver.find_element(By.CSS_SELECTOR, self.level_ref).text.replace('.', ''))
        except:
            try:
                self.level = int(self.driver.find_element(By.CSS_SELECTOR,
                                                          self.blocked_level_ref).text.replace('.', ''))
            except:
                print(Fore.RED + f'Не смогли получить уровень {self.name} '
                                 f'time ({datetime.datetime.now().strftime("%H:%M:%S")})')
                print(Style.RESET_ALL)

    def get_available(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.ref_to_upgrade_button)
            self.available_to_upgrade = True
        except:
            self.available_to_upgrade = False
