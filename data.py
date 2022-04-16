#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Mines.Mines import *
from Mines.Storages import *
from Factories.Factories import *
from Technologies.Technology import *
from force_builder.Ships import *


class Colony:
    def __init__(self, driver, data):
        self.colony_data = data
        self.driver = driver
        self.ref = ''


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
        self.Technologies['impulseDriveTechnology'] = ImpulseDriveTechnology(self.driver, self)
        self.Technologies['combustionDriveTechnology'] = CombustionDriveTechnology(self.driver, self)
        self.Technologies['ionTechnology'] = IonTechnology(self.driver, self)
        self.Technologies['laserTechnology'] = LaserTechnology(self.driver, self)
        self.Technologies['energyTechnology'] = EnergyTechnology(self.driver, self)

        self.Technologies['espionageTechnology'] = EspionageTechnology(self.driver, self)
        self.Technologies['computerTechnology'] = ComputerTechnology(self.driver, self)
        self.Technologies['astrophysicsTechnology'] = AstrophysicsTechnology(self.driver, self)

        self.Technologies['weaponsTechnology'] = WeaponsTechnology(self.driver, self)
        self.Technologies['armorTechnology'] = ArmorTechnology(self.driver, self)
        self.Technologies['shieldingTechnology'] = ShieldingTechnology(self.driver, self)

    Technologies: dict[str, Technology] = {

    }

    Colonies: dict[str, Colony] = {

    }

    Server: str = 'Tarazed'

    Login: str = '665577448833a@gmail.com'
    Password: str = 'LoginAdmin1765'

    Login1: str = '2211pozan1122@gmail.com'
    Password1: str = 'LoginAdmin1765'


class ColonyData:
    """
        Object that contains data dependent from planet ( buildings, resources and e.t.c)
    """
    def __init__(self, driver):
        self.driver = driver
        self.set_objects_in_dicts()

    def set_objects_in_dicts(self):
        """
            Generate Mines, storages, fabrics and ships objects Set them in dicts
        :return: nothing
        """
        #  Mines
        self.Mines['metalMine'] = MetalMine(self.driver, self)
        self.Mines['crystalMine'] = CrystallMine(self.driver, self)
        self.Mines['deuteriumSynthesizer'] = DeuteriumMine(self.driver, self)
        self.Mines['SolarMine'] = SolarMine(self.driver, self)
        #  Storages
        self.Storages['metalStorage'] = MetalStorage(self.driver, self)
        self.Storages['crystalStorage'] = CrystalStorage(self.driver, self)
        self.Storages['deuteriumStorage'] = DeuteriumStorage(self.driver, self)
        self.Storages['solarStorage'] = SolarStorage(self.driver, self)
        # Fabrics
        self.Factories['roboticsFactory'] = RoboticFactory(self.driver, self)
        self.Factories['researchLaboratory'] = ResearchLaboratory(self.driver, self)
        self.Factories['shipyard'] = Shipyard(self.driver, self)
        # Ships
        self.Ships['fighterLight'] = FighterLight(self.driver, self)
        self.Ships['fighterHeavy'] = FighterHeavy(self.driver, self)
        self.Ships['cruiser'] = Cruiser(self.driver, self)
        self.Ships['battleship'] = Battleship(self.driver, self)
        self.Ships['interceptor'] = Interceptor(self.driver, self)
        self.Ships['bomber'] = Bomber(self.driver, self)
        self.Ships['destroyer'] = Destroyer(self.driver, self)
        self.Ships['reaper'] = Reaper(self.driver, self)
        self.Ships['espionageProbe'] = EspionageProbe(self.driver, self)
        self.Ships['transporterSmall'] = TransporterSmall(self.driver, self)
        self.Ships['resbuggy'] = Resbuggy(self.driver, self)
        self.Ships['colonyShip'] = ColonyShip(self.driver, self)

    Mines: dict[str, Building] = {

    }

    Storages: dict[str, Building] = {

    }

    Factories: dict[str, Building] = {

    }

    Ships: dict[str, ForceUnit] = {

    }
