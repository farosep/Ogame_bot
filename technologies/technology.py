#! /usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import Fore, Style
from selenium.webdriver.common.by import By
from building import Building
import datetime
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException
)


class Technology(Building):
    """
        Main class for technologies objects
    """
    def __init__(
            self,
            driver
    ) -> None:
        super().__init__(driver)
        self.page = (
            'https://s146-ru.ogame.gameforge.com/'
            'game/index.php?page=ingame&component=research'
        )

    def try_to_upgrade(self) -> bool:
        """
            Check if tech available for upgrade and upgrade it
        :return:
        """
        if self.available_to_upgrade:
            try:
                self.driver.get(self.page)
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    self.ref_to_upgrade_button
                ).click()
                print(
                    Fore.BLUE +
                    f'{self.name} technology start to research '
                    f'at {datetime.datetime.now().strftime("%H:%M:%S")}'
                )
                print(Style.RESET_ALL)
                return True
            except NoSuchElementException or ElementNotInteractableException:
                print(
                    Fore.RED +
                    f'{self.name} technology was NOT started to research '
                    f'at {datetime.datetime.now().strftime("%H:%M:%S")}')
                print(Style.RESET_ALL)
        return False


class EnergyTechnology(Technology):
    """
        This is class for Energy Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.energyTechnology > button'
        self.name = 'energyTechnology'

    def try_to_upgrade(self) -> bool:
        """
            Additional check for level, because 8 level is the max needed
        :return: bool
        """
        if self.level < 8:
            if self.try_to_upgrade():
                return True
        return False


class EspionageTechnology(Technology):
    """
        This is class for Espionage Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.espionageTechnology > button'
        self.name = 'espionageTechnology'


class ComputerTechnology(Technology):
    """
        This is class for Computer Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.computerTechnology > button'
        self.name = 'computerTechnology'


class WeaponsTechnology(Technology):
    """
        This is class for Weapons Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.weaponsTechnology > button'
        self.name = 'weaponsTechnology'


class ArmorTechnology(Technology):
    """
        This is class for Armor Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.armorTechnology > button'
        self.name = 'armorTechnology'


class LaserTechnology(Technology):
    """
        This is class for Laser Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.laserTechnology > button'
        self.name = 'laserTechnology'

    def try_to_upgrade(self) -> bool:
        """
            Additional check for level, because 12 level is the max needed
        :return: bool
        """
        if self.level < 12:
            if self.try_to_upgrade():
                return True
        return False


class CombustionDriveTechnology(Technology):
    """
        This is class for CombustionDrive Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.combustionDriveTechnology > button'
        self.name = 'combustionDriveTechnology'


class ImpulseDriveTechnology(Technology):
    """
        This is class for ImpulseDrive Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.impulseDriveTechnology > button'
        self.name = 'impulseDriveTechnology'


class ShieldingTechnology(Technology):
    """
        This is class for Shielding Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.shieldingTechnology > button'
        self.name = 'shieldingTechnology'


class IonTechnology(Technology):
    """
        This is class for Ion Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.ionTechnology > button'
        self.name = 'ionTechnology'


class AstrophysicsTechnology(Technology):
    """
        This is class for Astrophysics Tech with its own parameters
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.ref_to_upgrade_button = 'span.astrophysicsTechnology > button'
        self.name = 'astrophysicsTechnology'
