#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Building import Building


class SolarMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.data = data
        self.ref_to_upgrade_button = 'span.solarPlant > button'
        self.name = 'solarPlant'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource <= 0:
            if super().try_to_upgrade():
                return True
        return False

    def get_level(self):
        pass


class MetalMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.data = data
        self.ref_to_upgrade_button = 'span.metalMine > button:nth-child(1)'
        self.name = 'metalMine'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource > 0 and self.level < self.data.Mines['CrystalMine'].level+2:
            if super().try_to_upgrade():
                return True
        return False


class CrystallMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.crystalMine > button:nth-child(1)'
        self.name = 'crystalMine'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource > 0 and self.level <= self.data.Mines['DeuteriumMine'].level + 3:
            if super().try_to_upgrade():
                return True
        return False


class DeuteriumMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.deuteriumSynthesizer > button:nth-child(1)'
        self.name = 'deuteriumSynthesizer'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource > 0 and self.level <= self.data.Mines['CrystalMine'].level - 3:
            if super().try_to_upgrade():
                return True
        return False
