#! /usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import Fore, Style
from selenium.webdriver.common.by import By
from Building import Building
import datetime


class Technology(Building):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.page = 'https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=research'

    def try_to_upgrade(self):
        self.colony_data = self.main_data.Colonies['Colony1'].colony_data
        if self.available_to_upgrade and self.colony_data.Factories['researchLaboratory'].available_to_use:
            try:
                self.driver.get(self.page)
                self.driver.find_element(By.CSS_SELECTOR, self.ref_to_upgrade_button).click()
                print(Fore.BLUE + f'{self.name} technology start to research {datetime.datetime.now().strftime("%H:%M:%S")}')
                print(Style.RESET_ALL)
                return True
            except:
                print(Fore.RED + f'{self.name} technology was NOT started to research {datetime.datetime.now().strftime("%H:%M:%S")}')
                print(Style.RESET_ALL)
        return False


class EnergyTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.energyTechnology > button'
        self.name = 'energyTechnology'

    def try_to_upgrade(self):
        if self.level < 8:
            if super().try_to_upgrade():
                return True
        return False


class EspionageTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.espionageTechnology > button'
        self.name = 'espionageTechnology'


class ComputerTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.computerTechnology > button'
        self.name = 'computerTechnology'


class WeaponsTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.weaponsTechnology > button'
        self.name = 'weaponsTechnology'


class ArmorTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.armorTechnology > button'
        self.name = 'armorTechnology'


class LaserTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.laserTechnology > button'
        self.name = 'laserTechnology'

    def try_to_upgrade(self):
        if self.level < 12:
            if super().try_to_upgrade():
                return True
        return False


class CombustionDriveTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.combustionDriveTechnology > button'
        self.name = 'combustionDriveTechnology'


class ImpulseDriveTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.impulseDriveTechnology > button'
        self.name = 'impulseDriveTechnology'


class ShieldingTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.shieldingTechnology > button'
        self.name = 'shieldingTechnology'


class IonTechnology(Technology):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.ref_to_upgrade_button = 'span.ionTechnology > button'
        self.name = 'ionTechnology'