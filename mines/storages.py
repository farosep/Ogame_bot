#! /usr/bin/env python
# -*- coding: utf-8 -*-
import selenium.webdriver
from building import Building
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import datetime
from selenium.common.exceptions import NoSuchElementException


class Storage(Building):
    """
        Base class for storages, that contains info about resources
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        super().__init__(driver)
        self.resource: int = 0
        self.resource_ref: str = ""
        self.resource_income: int = 0
        self.resource_income_ref: str = ""
        self.capacity: int = 9999999999
        self.capacity_ref: str = ""
        self.overexcited_capacity_ref: str = ""

    def get_resource(self) -> None:
        """
            Get amount of colony resources to self resource
        :return: None
        """
        try:
            self.resource = int(
                self.driver.find_element(
                    By.ID,
                    self.resource_ref
                ).text.replace(".", ""))
        except NoSuchElementException:
            print(
                Fore.RED + f"Didn't get amount of {self.name}  at "
                           f"time ({datetime.datetime.now().strftime('%H:%M:%S')})")
            print(Style.RESET_ALL)
            self.resource = 0

    def get_resource_income(self) -> None:
        """
            Get amount of colony resources income to self resource income
        :return: None
        """
        try:
            self.resource_income = int(
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    self.resource_income_ref
                ).text.replace(".", ""))
        except NoSuchElementException:
            print(Fore.RED + f"Didn't get income {self.name}")
            print(Style.RESET_ALL)
            self.resource_income = 0

    def get_resource_capacity(self) -> None:
        """
            Get storage's capacity info to self
        :return: bool
        """
        try:
            self.capacity = int(
                self.driver.find_element(
                    By.XPATH,
                    self.capacity_ref
                ).text.replace(".", ""))
        except NoSuchElementException:
            print(
                Fore.RED +
                f"Didn't get capacity {self.name}  "
                f"time ({datetime.datetime.now().strftime('%H:%M:%S')})"
            )
            print(Style.RESET_ALL)

    def try_to_upgrade(self) -> bool:
        """
            Check storage's capacity with income/amount and upgrade if capacity is smaller
        :return: bool
        """
        if (self.capacity < self.resource or
                self.capacity < self.resource_income * 8):
            if super().try_to_upgrade():
                return True
        return False


class MetalStorage(Storage):
    """
        Storage object that keeps info about metal capacity, amount, income
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        super().__init__(driver)
        self.ref_to_upgrade_button = "span.metalStorage > button:nth-child(1)"
        self.name = "metalStorage"
        self.capacity_ref = (
            "//*[contains(text(), 'Вместимость')]//"
            "following-sibling::td[1]//child::span")
        self.resource_ref = "resources_metal"
        self.resource_income_ref = ".summary > td:nth-child(2) > span:nth-child(1)"


class CrystalStorage(Storage):
    """
        Storage object that keeps info about crystal capacity, amount, income
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        super().__init__(driver)
        self.ref_to_upgrade_button = "span.crystalStorage > button:nth-child(1)"
        self.name = "crystalStorage"
        self.capacity_ref = (
            "//*[contains(text(), 'Вместимость')]//following-sibling::td[2]//child::span"
        )
        self.resource_ref = "resources_crystal"
        self.resource_income_ref = ".summary > td:nth-child(3) > span:nth-child(1)"


class DeuteriumStorage(Storage):
    """
        Storage object that keeps info about deuterium capacity, amount, income
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        super().__init__(driver)
        self.ref_to_upgrade_button = "span.deuteriumStorage > button:nth-child(1)"
        self.name = "deuteriumStorage"
        self.capacity_ref = (
            "//*[contains(text(), 'Вместимость')]//following-sibling::td[3]//child::span"
        )
        self.resource_ref = "resources_deuterium"
        self.resource_income_ref = ".summary > td:nth-child(4) > span:nth-child(1)"


class SolarStorage(Storage):
    """
        Fake storage object that keeps info about energy amount
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        super().__init__(driver)
        self.resource_ref = "resources_energy"
        self.name = "energy"

    def try_to_upgrade(self) -> bool:
        """
            Fake func for fake object
        :return:
        """
        return False

    def get_resource_capacity(self) -> None:
        """
            Fake func for fake object
        :return: None
        """
        pass

    def get_resource_income(self) -> None:
        """
            Fake func for fake object
        :return: None
        """
        pass
