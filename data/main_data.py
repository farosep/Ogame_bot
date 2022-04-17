#! /usr/bin/env python
# -*- coding: utf-8 -*-
from technologies.technology import (
    Technology,
    EnergyTechnology,
    EspionageTechnology,
    ComputerTechnology,
    WeaponsTechnology,
    ArmorTechnology,
    LaserTechnology,
    CombustionDriveTechnology,
    ImpulseDriveTechnology,
    ShieldingTechnology,
    IonTechnology,
    AstrophysicsTechnology
)
from data.colony_data import Colony


class MainData:
    """
        Object that contains data independent of planets and actual for user
    """
    def __init__(self, driver) -> None:
        self.driver = driver
        self.set_tech_in_dicts()

    def set_tech_in_dicts(self):
        """
            Generate technology objects and set them on their places in dict
        :return: nothing
        """
        self.Technologies["impulseDriveTechnology"] = ImpulseDriveTechnology(self.driver)
        self.Technologies["combustionDriveTechnology"] = CombustionDriveTechnology(
            self.driver
        )
        self.Technologies["ionTechnology"] = IonTechnology(self.driver)
        self.Technologies["laserTechnology"] = LaserTechnology(self.driver)
        self.Technologies["energyTechnology"] = EnergyTechnology(self.driver)

        self.Technologies["espionageTechnology"] = EspionageTechnology(self.driver)
        self.Technologies["computerTechnology"] = ComputerTechnology(self.driver)
        self.Technologies["astrophysicsTechnology"] = AstrophysicsTechnology(self.driver)

        self.Technologies["weaponsTechnology"] = WeaponsTechnology(self.driver)
        self.Technologies["armorTechnology"] = ArmorTechnology(self.driver)
        self.Technologies["shieldingTechnology"] = ShieldingTechnology(self.driver)

    Technologies: dict[str, Technology] = {

    }

    Colonies: dict[str, Colony] = {

    }

    Server: str = "Tarazed"

    Login: str = "665577448833a@gmail.com"
    Password: str = "LoginAdmin1765"

    Login1: str = "2211pozan1122@gmail.com"
    Password1: str = "LoginAdmin1765"


