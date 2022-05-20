from colorama import Fore, Style
from selenium.webdriver.common.by import By
import datetime
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver


class ForceUnit:
    """
        Base class for ships and defence platforms
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox,
            colony_data
    ) -> None:
        self.driver = driver
        self.colony_data = colony_data
        self.amount: int = 0
        self.amount_ref: str = ""
        self.name: str = ""
        self.available: bool = False
        self.build_button: str = ""
        self.need_amount: int = 0
        self.cost_in_metal: int = 0
        self.cost_in_crystal: int = 0
        self.cost_in_deuterium: int = 0
        self.resource_hold: int = 0

    def get_amount(self) -> None:
        """
            Get amount of current unit and save it in object
        :return: Nothing
        """
        try:
            self.amount = int(
                self.driver.find_element(
                    By.CSS_SELECTOR, self.amount_ref
                ).text)
        except NoSuchElementException:
            self.amount = 0
            print(Fore.RED + f"Didn't get amount of {self.name} "
                             f"at ({datetime.datetime.now().strftime('%H:%M:%S')})")
            print(Style.RESET_ALL)

    def get_available(self) -> None:
        """
            Get available param and set it in object
        :return: Nothing
        """
        try:
            a = self.driver.find_element(
                By.CSS_SELECTOR, self.build_button
            ).get_attribute("data-status")
            if a == "on":
                self.available = True
            else:
                self.available = False
        except NoSuchElementException:
            self.available = False

    def try_to_build(self) -> bool:
        """
            Func check available of unit, shipyard and need amount
            than builds missing units
        :return: bool
        """
        if (self.available and
                self.colony_data.Factories["shipyard"].available_to_use and
                self.need_amount > self.amount):
            try:
                self.driver.get(
                    "https://s146-ru.ogame.gameforge.com/"
                    "game/index.php?page=ingame&component=shipyard"
                )
                self.driver.find_element(By.CSS_SELECTOR, self.build_button).click()
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#build_amount"
                ).send_keys(f"{round(self.need_amount - self.amount)}")
                self.driver.find_element(By.CSS_SELECTOR, "span.tooltip").click()
                return True
            except NoSuchElementException:
                print(Fore.RED + f"Can't build {self.need_amount} {self.name} "
                                 f"at ({datetime.datetime.now().strftime('%H:%M:%S')})")
                print(Style.RESET_ALL)
        return False

    def get_need_amount(self) -> None:
        """
            Gets need amount of units in proportion of resources income
        :return:
        """
        self.need_amount = ((
            self.colony_data.Storages["metalStorage"].resource_income +
            self.colony_data.Storages["crystalStorage"].resource_income * 2 +
            self.colony_data.Storages["deuteriumStorage"].resource_income * 3) / (
                self.cost_in_metal + self.cost_in_crystal*2 + self.cost_in_deuterium*3
        ) * 10)
