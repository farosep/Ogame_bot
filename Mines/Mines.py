#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Building import Building


class SolarMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.data = data
        self.ref_to_upgrade_button = 'span.solarPlant > button'
        self.name = 'SolarMine'

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
        self.name = 'MetalMine'
        self.level_ref = 'span.metalMine > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.metalMine > span:nth-child(1) > span:nth-child(1)'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource > 0 and self.level < self.data.Mines['CrystalMine'].level+2:
            if super().try_to_upgrade():
                return True
        return False


class CrystallMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.crystalMine > button:nth-child(1)'
        self.name = 'CrystalMine'
        self.level_ref = 'span.crystalMine > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.crystalMine > span:nth-child(1) > span:nth-child(1)'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource > 0 and self.level <= self.data.Mines['DeuteriumMine'].level + 3:
            if super().try_to_upgrade():
                return True
        return False


class DeuteriumMine(Building):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.ref_to_upgrade_button = 'span.deuteriumSynthesizer > button:nth-child(1)'
        self.name = 'DeuteriumMine'
        self.level_ref = 'span.deuteriumSynthesizer > span:nth-child(2) > span:nth-child(1)'
        self.blocked_level_ref = 'span.deuteriumSynthesizer > span:nth-child(1) > span:nth-child(1)'

    def try_to_build(self):
        if self.data.Storages['solarStorage'].resource > 0 and self.level <= self.data.Mines['CrystalMine'].level - 3:
            if super().try_to_upgrade():
                return True
        return False
