#! /usr/bin/env python
# -*- coding: utf-8 -*-
from building import Building
from colorama import Fore, Style
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException
)
import selenium.webdriver


class Factory(Building):
    """
        Base class for factory buildings
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        super().__init__(driver)
        self.page = (
            "https://s146-ru.ogame.gameforge.com/"
            "game/index.php?page=ingame&component=facilities"
        )
        self.available_to_use: bool = False
        self.available_to_use_ref: str = ""

    def try_to_upgrade(self) -> bool:
        """
            Check is factory available and upgrade if it is
        :return: bool
        """
        if self.available_to_upgrade:
            try:
                self.driver.get(self.page)
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    self.ref_to_upgrade_button
                ).click()
                print(Fore.BLUE + f"{self.name} factory was built")
                print(Style.RESET_ALL)
                return True
            except NoSuchElementException or ElementNotInteractableException:
                print(Fore.RED + f"{self.name} factory was NOT built")
                print(Style.RESET_ALL)
        return False

    def get_level(self) -> None:
        """
            Fake func, because factory levels are useless
        :return: Nothing
        """
        pass

    def get_available_to_use(self) -> None:
        """
            Check is something already in queue, if not - marks true
        :return: Nothing
        """
        try:
            if self.driver.find_element(By.XPATH, self.available_to_use_ref) is not None:
                self.available_to_use = True
            else:
                self.available_to_use = False
        except NoSuchElementException:
            self.available_to_use = False


class RoboticFactory(Factory):
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ):
        super().__init__(driver)
        self.ref_to_upgrade_button: str = "span.roboticsFactory > button"
        self.name: str = "roboticsFactory"


class ResearchLaboratory(Factory):
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ):
        super().__init__(driver)
        self.ref_to_upgrade_button: str = "span.researchLaboratory > button"
        self.name: str = "researchLaboratory"
        self.available_to_use_ref: str = "//*[contains(text(), 'Не ведется никаких')]"


class Shipyard(Factory):
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ):
        super().__init__(driver)
        self.ref_to_upgrade_button: str = "span.shipyard > button"
        self.name: str = "shipyard"
        self.available_to_use_ref: str = "//*[contains(text(), 'Корабли')]"
