#! /usr/bin/env python
# -*- coding: utf-8 -*-
import selenium.webdriver
from colorama import Fore, Style
from selenium.webdriver.common.by import By
import datetime
from selenium.common.exceptions import (
    NoSuchElementException,
    NoSuchAttributeException,
    ElementNotInteractableException
)


class Building:
    """
        Base class for most objects in colonies ( mines, tech, factories etc)
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox
    ) -> None:
        self.driver = driver
        self.ref_to_upgrade_button: str = ""
        self.level: int = 0
        self.name: str = ""
        self.available_to_upgrade: bool = False
        self.page: str = (
            "https://s146-ru.ogame.gameforge.com/"
            "game/index.php?page=ingame&component=supplies"
        )

    def try_to_upgrade(self) -> bool:
        """
            This func try to start building upgrade and return result in bool
        :return: Bool
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
                    f"{self.name} mine was built "
                    f"at {datetime.datetime.now().strftime('%H:%M:%S')}"
                )
                print(Style.RESET_ALL)
                return True
            except ElementNotInteractableException or NoSuchElementException:
                print(
                    Fore.RED +
                    f"{self.name} Mine was NOT built "
                    f"at {datetime.datetime.now().strftime('%H:%M:%S')}")
                print(Style.RESET_ALL)
        return False

    def get_info(self) -> None:
        """
            Func to unite get level and get available
        :return: None
        """
        self.get_level()
        self.get_available()

    def get_level(self) -> None:
        """
            Func to get buildings level
        :return: None
        """
        try:
            self.level = int(
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    f"span.{self.name} > span"
                ).get_attribute("data-value"))
        except NoSuchElementException or NoSuchAttributeException:
            print(
                Fore.RED +
                f"Didn't get level of {self.name} "
                f"at ({datetime.datetime.now().strftime('%H:%M:%S')})")
            print(Style.RESET_ALL)

    def get_available(self) -> None:
        """
            Func to get buildings available to upgrade
        :return: Nothing
        """
        try:
            self.driver.find_element(
                By.CSS_SELECTOR,
                self.ref_to_upgrade_button
            )
            self.available_to_upgrade = True
        except NoSuchElementException:
            self.available_to_upgrade = False
