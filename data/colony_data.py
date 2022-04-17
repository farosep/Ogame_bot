from force_builder.ships import (
    ForceUnit,
    FighterLight,
    FighterHeavy,
    Cruiser,
    Battleship,
    Interceptor,
    Bomber,
    Destroyer,
    Reaper,
    Resbuggy,
    EspionageProbe,
    TransporterSmall,
    ColonyShip,
)
from mines.mines import (
    MetalMine,
    CrystalMine,
    DeuteriumMine,
    SolarMine,
    Building
)
from mines.storages import (
    MetalStorage,
    CrystalStorage,
    DeuteriumStorage,
    SolarStorage,
    Storage
)
from factories.factories import (
    RoboticFactory,
    Shipyard,
    ResearchLaboratory,
    Factory
)
from data.main_data import MainData


class ColonyData:
    """
        Object that contains data dependent from planet ( buildings, resources and e.t.c)
    """
    def __init__(self, driver, main_data: MainData):
        self.main_data = main_data
        self.driver = driver
        self.set_objects_in_dicts()

    def set_objects_in_dicts(self):
        """
            Generate mines, storages, fabrics and ships objects Set them in dicts
        :return: nothing
        """
        #  mines
        self.Mines["metalMine"] = MetalMine(self.driver, self)
        self.Mines["crystalMine"] = CrystalMine(self.driver, self)
        self.Mines["deuteriumSynthesizer"] = DeuteriumMine(self.driver, self)
        self.Mines["SolarMine"] = SolarMine(self.driver, self)
        #  Storages
        self.Storages["metalStorage"] = MetalStorage(self.driver)
        self.Storages["crystalStorage"] = CrystalStorage(self.driver)
        self.Storages["deuteriumStorage"] = DeuteriumStorage(self.driver)
        self.Storages["solarStorage"] = SolarStorage(self.driver)
        # Fabrics
        self.Factories["roboticsFactory"] = RoboticFactory(self.driver, self)
        self.Factories["researchLaboratory"] = ResearchLaboratory(self.driver, self)
        self.Factories["shipyard"] = Shipyard(self.driver, self)
        # Ships
        self.Ships["fighterLight"] = FighterLight(self.driver, self)
        self.Ships["fighterHeavy"] = FighterHeavy(self.driver, self)
        self.Ships["cruiser"] = Cruiser(self.driver, self)
        self.Ships["battleship"] = Battleship(self.driver, self)
        self.Ships["interceptor"] = Interceptor(self.driver, self)
        self.Ships["bomber"] = Bomber(self.driver, self)
        self.Ships["destroyer"] = Destroyer(self.driver, self)
        self.Ships["reaper"] = Reaper(self.driver, self)
        self.Ships["espionageProbe"] = EspionageProbe(self.driver, self)
        self.Ships["transporterSmall"] = TransporterSmall(self.driver, self)
        self.Ships["resbuggy"] = Resbuggy(self.driver, self)
        self.Ships["colonyShip"] = ColonyShip(self.driver, self)

    Mines: dict[str, Building] = {

    }

    Storages: dict[str, Storage] = {

    }

    Factories: dict[str, Factory] = {

    }

    Ships: dict[str, ForceUnit] = {

    }


class Colony:
    def __init__(self, driver, data: ColonyData):
        self.colony_data = data
        self.driver = driver
        self.ref = ""
