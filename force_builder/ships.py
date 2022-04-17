from force_builder.force_builder import ForceUnit


class FighterLight(ForceUnit):
    """
        Light fighter object with its own params like cost
    """
    def __init__(self, driver, colony_data):
        """

        :param driver: Browser driver for selenium
        :param data: colony_data object
        """
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.fighterLight > span:nth-child(1) > span:nth-child(1)'
        self.name = 'fighterLight'
        self.build_button = 'li.fighterLight'
        self.cost_in_metal = 3000
        self.cost_in_crystal = 1000


class FighterHeavy(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.fighterHeavy > span:nth-child(1) > span:nth-child(1)'
        self.name = 'fighterHeavy'
        self.build_button = 'li.fighterHeavy'
        self.cost_in_metal = 6000
        self.cost_in_crystal = 4000


class Cruiser(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.cruiser > span:nth-child(1) > span:nth-child(1)'
        self.name = 'cruiser'
        self.build_button = 'li.cruiser'
        self.cost_in_metal = 20000
        self.cost_in_crystal = 7000
        self.cost_in_deuterium = 2000


class Battleship(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.battleship > span:nth-child(1) > span:nth-child(1)'
        self.name = 'battleship'
        self.build_button = 'li.battleship'
        self.cost_in_metal = 45000
        self.cost_in_crystal = 15000


class Interceptor(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.interceptor > span:nth-child(1) > span:nth-child(1)'
        self.name = 'interceptor'
        self.build_button = 'li.interceptor'
        self.cost_in_metal = 30000
        self.cost_in_crystal = 40000
        self.cost_in_deuterium = 15000


class Bomber(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.bomber > span:nth-child(1) > span:nth-child(1)'
        self.name = 'bomber'
        self.build_button = 'li.bomber'
        self.cost_in_metal = 50000
        self.cost_in_crystal = 25000
        self.cost_in_deuterium = 15000


class Destroyer(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.destroyer > span:nth-child(1) > span:nth-child(1)'
        self.name = 'destroyer'
        self.build_button = 'li.destroyer'
        self.cost_in_metal = 60000
        self.cost_in_crystal = 50000
        self.cost_in_deuterium = 15000


class Reaper(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.reaper > span:nth-child(1) > span:nth-child(1)'
        self.name = 'reaper'
        self.build_button = 'li.reaper'
        self.cost_in_metal = 85000
        self.cost_in_crystal = 55000
        self.cost_in_deuterium = 20000


class Resbuggy(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.resbuggy > span:nth-child(1) > span:nth-child(1)'
        self.name = 'resbuggy'
        self.build_button = 'li.resbuggy'
        self.cost_in_metal = 2000
        self.cost_in_crystal = 2000
        self.cost_in_deuterium = 1000


class EspionageProbe(ForceUnit):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.amount_ref = 'span.espionageProbe > span:nth-child(1) > span:nth-child(1)'
        self.name = 'espionageProbe'
        self.build_button = 'li.espionageProbe'
        self.cost_in_crystal = 1000

    def get_need_amount(self):
        self.need_amount = (self.colony_data.main_data.Technologies['computerTechnology'].level + 1) * 5


class TransporterSmall(ForceUnit):
    def __init__(self, driver, colony_data):
        super().__init__(driver, colony_data)
        self.amount_ref = 'span.transporterSmall > span:nth-child(1) > span:nth-child(1)'
        self.name = 'transporterSmall'
        self.build_button = 'li.transporterSmall'
        self.cost_in_crystal = 2000
        self.cost_in_metal = 2000
        self.resource_hold = 5000

    def get_need_amount(self):
        self.need_amount = (self.colony_data.Storages['metalStorage'].resource +
                            self.colony_data.Storages['crystalStorage'].resource +
                            self.colony_data.Storages['deuteriumStorage'].resource) / self.resource_hold


class ColonyShip(ForceUnit):
    def __init__(self, driver, main_data):
        super().__init__(driver, main_data)
        self.amount_ref = 'span.colonyShip > span:nth-child(1) > span:nth-child(1)'
        self.name = 'colonyShip'
        self.build_button = 'li.colonyShip  '
        self.cost_in_crystal = 10000
        self.cost_in_metal = 20000
        self.resource_hold = 10000

    def get_need_amount(self):
        self.need_amount = (round(self.colony_data.main_data.Technologies['astrophysicsTechnology'].level/2)) \
                           - len(self.colony_data.main_data.Colonies) + 1 - self.amount
