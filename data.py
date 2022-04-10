

class data():
    #  Ресурсы игрока
    resources = {
        'metal': None,
        'crystal': None,
        'deuterium': None,
        'energy': None
    }
    #  Ссылки на ресурсы игрока
    resources_refs = {
        'metal': 'resources_metal',
        'crystal': 'resources_crystal',
        'deuterium': 'resources_deuterium',
        'energy': 'resources_energy'
    }

    #  Прирост ресурсов в час
    resources_income = {
        'metal_income': 0,
        'crystal_income': 0,
        'deuterium_income': 0
    }

    # Ссылки на прирост ресурсов
    mine_income_refs = {
        'metal_income': '.summary > td:nth-child(2) > span:nth-child(1)',
        'crystal_income': '.summary > td:nth-child(3) > span:nth-child(1)',
        'deuterium_income': '.summary > td:nth-child(4) > span:nth-child(1)'
    }

    #  Вместимость хранилищ
    resources_storages = {
        'metal_storage': 99999999999,
        'crystal_storage': 99999999999,
        'deuterium_storage': 99999999999
    }

    #  Ссылки на вместимость хранилищ
    mine_capacity_refs = {
        'metal_storage': 'td.normalmark:nth-child(2) > span:nth-child(1)',
        'crystal_storage': 'td.left2:nth-child(3) > span:nth-child(1)',
        'deuterium_storage': 'td.left2:nth-child(4) > span:nth-child(1)'
    }

    # Ссылки на переполненную вместимость хранилищ
    mine_overexcited_capacity_refs = {
        'metal_storage': 'td.overmark:nth-child(2) > span',
        'crystal_storage': 'td.overmark:nth-child(3) > span',
        'deuterium_storage': 'td.overmark:nth-child(4) > span'
    }

    #  Уровни шахт
    mine_levels = {
        'metal_mine_level': None,
        'crystal_mine_level': None,
        'deuterium_mine_level': None
    }

    # Ссылки на уровни шахт
    mine_level_refs = {
        'metal_mine_level': 'span.metalMine > span:nth-child(2) > span:nth-child(1)',
        'crystal_mine_level': 'span.crystalMine > span:nth-child(2) > span:nth-child(1)',
        'deuterium_mine_level': 'span.deuteriumSynthesizer > span:nth-child(2) > span:nth-child(1)'
    }

    #  Ссылки на уровень заблокированных к постройке шахт
    blocked_mine_level_refs = {
        'metal_mine_level': 'span.metalMine > span:nth-child(1) > span:nth-child(1)',
        'crystal_mine_level': 'span.crystalMine > span:nth-child(1) > span:nth-child(1)',
        'deuterium_mine_level': 'span.deuteriumSynthesizer > span:nth-child(1) > span:nth-child(1)'
    }

    #  Доступные к постройке шахты
    Mines_available_to_build = {
        'metal_mine': False,
        'crystal_mine': False,
        'deuterium_mine': False,
        'SolarEnergy_mine': False,
        'metal_storage': False,
        'crystal_storage': False,
        'deuterium_storage': False
    }

    #  Список кнопок улучшения шахт
    Upgrade_mines_buttons = {
        'metal_mine': 'span.metalMine > button:nth-child(1)',
        'crystal_mine': 'span.crystalMine > button:nth-child(1)',
        'deuterium_mine': 'span.deuteriumSynthesizer > button:nth-child(1)',
        'SolarEnergy_mine': 'span.solarPlant > button:nth-child(1)',
        'metal_storage': 'span.metalStorage > button:nth-child(1)',
        'crystal_storage': 'span.crystalStorage > button:nth-child(1)',
        'deuterium_storage': 'span.deuteriumStorage > button:nth-child(1)'
    }

    #  Ссылки на улучшение фабрик
    Upgrade_factory_refs = {
        'roboticsFactory': 'span.roboticsFactory > button',
        'researchLaboratory': 'span.researchLaboratory > button',
        'shipyard': 'span.shipyard > button'
        }

    #  Ссылки на уровень фабрик
    Factory_level_refs = {
        'roboticsFactory': 'span.roboticsFactory > span > span:nth-child(1)',
        'researchLaboratory': 'span.researchLaboratory > span > span:nth-child(1)',
        'shipyard': 'span.shipyard > span > span:nth-child(1)'
    }

    # Ссылки на заблокированные уровни фабрик
    Blocked_factory_level_refs = {
        'roboticsFactory': 0,
        'researchLaboratory': 0,
        'shipyard': 0
    }

    #  Уровень фабрик
    Factory_levels = {
        'roboticsFactory': 0,
        'researchLaboratory': 0,
        'shipyard': 0
    }

    #  Фабрики доступные к постройке
    Factory_available_to_build = {
        'roboticsFactory': False,
        'researchLaboratory': False,
        'shipyard': False
    }

    #  Кнопки улучшения технологий
    Technologies_upgrade_buttons = {
        'energyTechnology': 'span.energyTechnology > button',
        'espionageTechnology': 'span.espionageTechnology > button',
        'computerTechnology': 'span.computerTechnology > button',
        'weaponsTechnology': 'span.weaponsTechnology > button',
        'armorTechnology': 'span.armorTechnology > button'
    }

    #  Уровни технологий
    Technologies_levels = {
        'energyTechnology': 0,
        'espionageTechnology': 0,
        'computerTechnology': 0,
        'weaponsTechnology': 0,
        'armorTechnology': 0
    }

    #  Ссылки на уровни технологий
    Technologies_levels_refs ={
        'energyTechnology': 'span.energyTechnology > span:nth-child(2) > span:nth-child(1)',
        'espionageTechnology': 'span.espionageTechnology > span:nth-child(2) > span:nth-child(1)',
        'computerTechnology': 'span.computerTechnology > span:nth-child(2) > span:nth-child(1)',
        'weaponsTechnology': 'span.weaponsTechnology > span:nth-child(2) > span:nth-child(1)',
        'armorTechnology': 'span.armorTechnology > span:nth-child(2) > span:nth-child(1)'
    }

    #  Ссылки на заблокированные уровни технологий
    Blocked_technologies_levels_refs = {
        'energyTechnology': 'span.energyTechnology > span:nth-child(1) > span:nth-child(1)',
        'espionageTechnology': 'span.espionageTechnology > span:nth-child(1) > span:nth-child(1)',
        'computerTechnology': 'span.computerTechnology > span:nth-child(1) > span:nth-child(1)',
        'weaponsTechnology': 'span.weaponsTechnology > span:nth-child(1) > span:nth-child(1)',
        'armorTechnology': 'span.armorTechnology > span:nth-child(1) > span:nth-child(1)'
    }

    #  Технологии которые можно улучшить
    Available_technologies = {
        'energyTechnology': False,
        'espionageTechnology': False,
        'computerTechnology': False,
        'weaponsTechnology': False,
        'armorTechnology': False
    }