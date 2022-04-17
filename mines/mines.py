#! /usr/bin/env python
# -*- coding: utf-8 -*-
import data.colony_data
from building import Building


class SolarMine(Building):
    """
        Building object that contains info about solar plant
    """
    def __init__(
            self,
            driver,
            colony_data: data.colony_data.ColonyData
    ) -> None:
        super().__init__(driver)
        self.colony_data = colony_data
        self.ref_to_upgrade_button = "span.solarPlant > button"
        self.name = "solarPlant"

    def try_to_upgrade(self) -> bool:
        """
            Additional check for negative energy and build
        :return: bool
        """
        if self.colony_data.Storages["solarStorage"].resource <= 0:
            if super().try_to_upgrade():
                return True
        return False

    def get_level(self):
        """
            Fake func because this data is useless
        :return: Nothing
        """
        pass


class MetalMine(Building):
    """
        Building object that contains info about metal mine
    """
    def __init__(
            self,
            driver,
            colony_data: data.colony_data.ColonyData
    ) -> None:
        super().__init__(driver)
        self.colony_data = colony_data
        self.ref_to_upgrade_button = "span.metalMine > button:nth-child(1)"
        self.name = "metalMine"

    def try_to_upgrade(self) -> bool:
        """
            Additional check for negative energy and level proportion with crystal mine
        :return: bool
        """
        if (self.colony_data.Storages["solarStorage"].resource > 0 and
                self.level < self.colony_data.Mines["CrystalMine"].level+2):
            if super().try_to_upgrade():
                return True
        return False


class CrystalMine(Building):
    """
        Building object that contains info about crystal mine
    """
    def __init__(
            self,
            driver,
            colony_data: data.colony_data.ColonyData
    ) -> None:
        super().__init__(driver)
        self.colony_data = colony_data
        self.ref_to_upgrade_button = "span.crystalMine > button:nth-child(1)"
        self.name = "crystalMine"

    def try_to_upgrade(self) -> bool:
        """
            Additional check for negative energy and level proportion with deuterium mine
        :return: bool
        """
        if (self.colony_data.Storages["solarStorage"].resource > 0 and
                self.level <= self.colony_data.Mines["DeuteriumMine"].level + 3):
            if super().try_to_upgrade():
                return True
        return False


class DeuteriumMine(Building):
    """
        Building object that contains info about deuterium mine
    """
    def __init__(
            self,
            driver,
            colony_data: data.colony_data.ColonyData
    ) -> None:
        super().__init__(driver)
        self.ref_to_upgrade_button = "span.deuteriumSynthesizer > button:nth-child(1)"
        self.name = "deuteriumSynthesizer"
        self.colony_data = colony_data

    def try_to_upgrade(self) -> bool:
        """
            Additional check for negative energy and level proportion with crystal mine
        :return: bool
        """
        if (self.colony_data.Storages["solarStorage"].resource > 0 and
                self.level <= self.colony_data.Mines["CrystalMine"].level - 3):
            if super().try_to_upgrade():
                return True
        return False
