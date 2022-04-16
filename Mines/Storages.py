#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Building import Building
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import datetime


class Storage(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.resource = 0
        self.resource_ref = ''
        self.resource_income = 0
        self.resource_income_ref = ''
        self.capacity = 9999999999
        self.capacity_ref = ''
        self.overexcited_capacity_ref = ''

    def get_resource(self):
        try:
            self.resource = int(self.driver.find_element(By.ID, self.resource_ref).text.replace('.', ''))
        except:
            print(
                Fore.RED + f'Не смогли найти количество ресурсов {self.name}  '
                           f'time ({datetime.datetime.now().strftime("%H:%M:%S")})')
            print(Style.RESET_ALL)
            self.resource = 0

    def get_resource_income(self):
        try:
            self.resource_income = int(
                self.driver.find_element(By.CSS_SELECTOR, self.resource_income_ref).text.replace('.', ''))
        except:
            print(Fore.RED + f'Не смогли получить прирост {self.name}')
            print(Style.RESET_ALL)
            self.resource_income = 0

    def get_resource_capacity(self):
        try:
            self.capacity = int(
                self.driver.find_element(By.XPATH, self.capacity_ref).text.replace('.', ''))
        except:
            print(Fore.RED + f'Не смогли получить размер хранилища {self.name}  '
                               f'time ({datetime.datetime.now().strftime("%H:%M:%S")})')
            print(Style.RESET_ALL)

    def try_to_upgrade(self):
        if (self.capacity < self.resource or self.capacity < self.resource_income * 8):
            if super().try_to_upgrade():
                return True
        return False


class MetalStorage(Storage):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.metalStorage > button:nth-child(1)'
        self.name = 'metalStorage'
        self.capacity_ref = '//*[contains(text(), "Вместимость")]//following-sibling::td[1]//child::span'
        self.resource_ref = 'resources_metal'
        self.resource_income_ref = '.summary > td:nth-child(2) > span:nth-child(1)'


class CrystalStorage(Storage):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.crystalStorage > button:nth-child(1)'
        self.name = 'crystalStorage'
        self.capacity_ref = '//*[contains(text(), "Вместимость")]//following-sibling::td[2]//child::span'
        self.resource_ref = 'resources_crystal'
        self.resource_income_ref = '.summary > td:nth-child(3) > span:nth-child(1)'


class DeuteriumStorage(Storage):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.deuteriumStorage > button:nth-child(1)'
        self.name = 'deuteriumStorage'
        self.capacity_ref = '//*[contains(text(), "Вместимость")]//following-sibling::td[3]//child::span'
        self.resource_ref = 'resources_deuterium'
        self.resource_income_ref = '.summary > td:nth-child(4) > span:nth-child(1)'


class SolarStorage(Storage):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.resource_ref = 'resources_energy'
        self.name = 'energy'

    def try_to_upgrade(self):
        return False

    def get_resource_capacity(self):
        pass

    def get_resource_income(self):
        pass
