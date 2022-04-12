#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Building import Building
from colorama import Fore, Style
from selenium.webdriver.common.by import By


class Factory(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.page = 'https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities'

    def try_to_upgrade(self):
        if self.available_to_upgrade:
            try:
                self.driver.get(self.page)
                self.driver.find_element(By.CSS_SELECTOR, self.ref_to_upgrade_button).click()
                print(Fore.BLUE + f'{self.name} factory was built')
                print(Style.RESET_ALL)
                return True
            except:
                print(Fore.RED + f'{self.name} factory was NOT built')
                print(Style.RESET_ALL)
        return False

    def get_level(self):
        pass


class RoboticFactory(Factory):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.roboticsFactory > button'
        self.name = 'roboticsFactory'


class ResearchLaboratory(Factory):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.researchLaboratory > button'
        self.name = 'researchLaboratory'


class Shipyard(Factory):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.shipyard > button'
        self.name = 'shipyard'
