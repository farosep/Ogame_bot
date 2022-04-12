from colorama import Fore, Style
from selenium.webdriver.common.by import By
import datetime
from Building import Building


class Technology(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.page = 'https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=research'

    def try_to_upgrade(self):
        if self.available_to_upgrade:
            try:
                self.driver.get(self.page)
                self.driver.find_element(By.CSS_SELECTOR, self.ref_to_upgrade_button).click()
                print(Fore.BLUE + f'{self.name} technology researched')
                print(Style.RESET_ALL)
                return True
            except:
                print(Fore.RED + f'{self.name} technology was NOT researched')
                print(Style.RESET_ALL)
        return False


class EnergyTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.energyTechnology > button'
        self.level_ref = 'span.energyTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.energyTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'energyTechnology'

    def try_to_upgrade(self):
        if self.level < 8:
            if super().try_to_upgrade():
                return True
        return False


class EspionageTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.espionageTechnology > button'
        self.level_ref = 'span.espionageTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.espionageTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'espionageTechnology'


class ComputerTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.computerTechnology > button'
        self.level_ref = 'span.computerTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.computerTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'computerTechnology'


class WeaponsTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.weaponsTechnology > button'
        self.level_ref = 'span.weaponsTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.weaponsTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'weaponsTechnology'


class ArmorTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.armorTechnology > button'
        self.level_ref = 'span.armorTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.armorTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'armorTechnology'


class LaserTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.laserTechnology > button'
        self.level_ref = 'span.laserTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.laserTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'laserTechnology'

    def try_to_upgrade(self):
        if self.level < 12:
            if super().try_to_upgrade():
                return True
        return False


class CombustionDriveTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.combustionDriveTechnology > button'
        self.level_ref = 'span.combustionDriveTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.combustionDriveTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'combustionDriveTechnology'


class ImpulseDriveTechnology(Technology):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.impulseDriveTechnology > button'
        self.level_ref = 'span.impulseDriveTechnology > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.impulseDriveTechnology > span:nth-child(1) > span:nth-child(1)'
        self.name = 'impulseDriveTechnology'
