

class Data:
    Mines = {
        'MetalMine': '',
        'CrystalMine': '',
        'DeuteriumMine': '',
        'SolarMine': ''
    }

    Storages = {
        'metalStorage': '',
        'crystalStorage': '',
        'deuteriumStorage': '',
        'solarStorage': ''
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
        'armorTechnology': 'span.armorTechnology > button',
        'laserTechnology': 'span.laserTechnology > button',
        'combustionDriveTechnology': 'span.combustionDriveTechnology > button',
        'impulseDriveTechnology': 'span.impulseDriveTechnology > button'
    }

    #  Уровни технологий
    Technologies_levels = {
        'energyTechnology': 0,
        'espionageTechnology': 0,
        'computerTechnology': 0,
        'weaponsTechnology': 0,
        'armorTechnology': 0,
        'laserTechnology': 0,
        'combustionDriveTechnology': 0,
        'impulseDriveTechnology': 0
    }

    #  Ссылки на уровни технологий
    Technologies_levels_refs = {
        'energyTechnology': 'span.energyTechnology > span:nth-child(2) > span:nth-child(1)',
        'espionageTechnology': 'span.espionageTechnology > span:nth-child(2) > span:nth-child(1)',
        'computerTechnology': 'span.computerTechnology > span:nth-child(2) > span:nth-child(1)',
        'weaponsTechnology': 'span.weaponsTechnology > span:nth-child(2) > span:nth-child(1)',
        'armorTechnology': 'span.armorTechnology > span:nth-child(2) > span:nth-child(1)',
        'laserTechnology': 'span.laserTechnology > span:nth-child(2) > span:nth-child(1)',
        'combustionDriveTechnology': 'span.combustionDriveTechnology > span:nth-child(2) > span:nth-child(1)',
        'impulseDriveTechnology': 'span.impulseDriveTechnology > span:nth-child(2) > span:nth-child(1)'
    }

    #  Ссылки на заблокированные уровни технологий
    Blocked_technologies_levels_refs = {
        'energyTechnology': 'span.energyTechnology > span:nth-child(1) > span:nth-child(1)',
        'espionageTechnology': 'span.espionageTechnology > span:nth-child(1) > span:nth-child(1)',
        'computerTechnology': 'span.computerTechnology > span:nth-child(1) > span:nth-child(1)',
        'weaponsTechnology': 'span.weaponsTechnology > span:nth-child(1) > span:nth-child(1)',
        'armorTechnology': 'span.armorTechnology > span:nth-child(1) > span:nth-child(1)',
        'laserTechnology': 'span.laserTechnology > span:nth-child(1) > span:nth-child(1)',
        'combustionDriveTechnology': 'span.combustionDriveTechnology > span:nth-child(1) > span:nth-child(1)',
        'impulseDriveTechnology': 'span.impulseDriveTechnology > span:nth-child(1) > span:nth-child(1)'
    }

    #  Технологии которые можно улучшить
    Available_technologies = {
        'energyTechnology': False,
        'espionageTechnology': False,
        'computerTechnology': False,
        'weaponsTechnology': False,
        'armorTechnology': False,
        'laserTechnology': False,
        'combustionDriveTechnology': False,
        'impulseDriveTechnology': False
    }

    Login = '665577448833a@gmail.com'
    Password = 'LoginAdmin1765'

    Login1 = '2211pozan1122@gmail.com'
    Password1 = 'LoginAdmin1765'