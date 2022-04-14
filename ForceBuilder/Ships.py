from ForceBuilder import ForceUnit


class FighterLight(ForceUnit):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.amount_ref = 'span.fighterLight > span:nth-child(1) > span:nth-child(1)'
        self.name = 'fighterLight'
        self.build_button = 'span.fighterLight'
        self.cost_in_metal = 3000
        self.cost_in_crystal = 1000


class EspionageProbe(ForceUnit):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.amount_ref = 'span.espionageProbe > span:nth-child(1) > span:nth-child(1)'
        self.name = 'espionageProbe'
        self.build_button = 'span.espionageProbe'
        self.cost_in_crystal = 1000

    def get_need_amount(self):
        self.need_amount = (self.data.Technologies['computerTechnology'].level + 1) * 5


class TransporterSmall(ForceUnit):
    def __init__(self, driver, data):
        super().__init__(driver, data)
        self.amount_ref = 'span.transporterSmall > span:nth-child(1) > span:nth-child(1)'
        self.name = 'transporterSmall'
        self.build_button = 'span.transporterSmall'
        self.cost_in_crystal = 2000
        self.cost_in_metal = 2000
        self.resource_hold = 5000

    def get_need_amount(self):
        self.need_amount = (self.data.Storages['metalStorage'].resource +
                           self.data.Storages['crystalStorage'].resource +
                           self.data.Storages['deuteriumStorage'].resource) / self.resource_hold