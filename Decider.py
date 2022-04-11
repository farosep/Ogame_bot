from selenium.webdriver.common.by import By
from colorama import Fore, Style


def decide_what_to_do(driver, data):
    if decide_what_tech_to_research(driver, data):
        if decide_what_factory_to_build(driver, data):
            decide_what_mine_to_build(driver, data)


def build_resource(driver, data, building_name):
    try:
        driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
        driver.find_element(By.CSS_SELECTOR, data.Upgrade_mines_buttons[building_name]).click()
        print(Fore.BLUE + f'{building_name} mine was built')
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + f'{building_name} Mine was NOT built')
        print(Style.RESET_ALL)


def build_factory(driver, data, building_name):
    try:
        driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
        driver.find_element(By.CSS_SELECTOR, data.Upgrade_factory_refs[building_name]).click()
        print(Fore.BLUE + f'{building_name} facility  was built')
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + f'{building_name} facility was NOT built')
        print(Style.RESET_ALL)


def decide_what_mine_to_build(driver, data):
    # условия постройки солнечной станции
    if data.resources['energy'] <= 0 and data.Mines_available_to_build['SolarEnergy_mine']:
        build_resource(driver, data, 'SolarEnergy_mine')
    #  Условия постройки металлической шахты
    elif (data.resources['energy'] > 0 and data.Mines_available_to_build['metal_mine']
          and data.mine_levels['metal_mine_level'] <= data.mine_levels['crystal_mine_level'] + 2):
        build_resource(driver, data, 'metal_mine')
    #  Условия постройки кристаллической шахты
    elif (data.resources['energy'] > 0 and data.Mines_available_to_build['crystal_mine']
          and data.mine_levels['crystal_mine_level'] <= data.mine_levels['deuterium_mine_level'] + 3):
        build_resource(driver, data, 'crystal_mine')
    #  Условия постройки дейтериевой шахты
    elif (data.resources['energy'] > 0 and data.Mines_available_to_build['deuterium_mine']
          and data.mine_levels['deuterium_mine_level'] < data.mine_levels['crystal_mine_level'] - 3):
        build_resource(driver, data, 'deuterium_mine')
    #  Условия постройки хранилища металла
    elif ((data.resources_income['metal_income']*8 > data.resources_storages['metal_storage']
          or data.resources['metal'] > data.resources_storages['metal_storage'])
          and data.Mines_available_to_build['metal_storage']):
        build_resource(driver, data, 'metal_storage')
    #  Условия постройки хранилища кристалла
    elif ((data.resources_income['crystal_income']*8 > data.resources_storages['crystal_storage']
           or data.resources['crystal'] > data.resources_storages['crystal_storage'])
          and data.Mines_available_to_build['crystal_storage']):
        build_resource(driver, data, 'crystal_storage')
    #  Условия постройки хранилища дейтерия
    elif ((data.resources_income['deuterium_income']*8 > data.resources_storages['deuterium_storage']
           or data.resources['deuterium'] > data.resources_storages['deuterium_storage']) and
          data.Mines_available_to_build['deuterium_storage']):
        build_resource(driver, data, 'deuterium_storage')
    else:
        return True


def decide_what_factory_to_build(driver, data):
    if data.Factory_available_to_build['researchLaboratory']:
        build_factory(driver, data, 'researchLaboratory')
    elif data.Factory_available_to_build['shipyard']:
        build_factory(driver, data, 'shipyard')
    elif data.Factory_available_to_build['roboticsFactory']:
        build_factory(driver, data, 'roboticsFactory')
    else:
        return True


def decide_what_tech_to_research(driver, data):
    if data.Available_technologies['espionageTechnology']:
        research_technology(driver, data, 'espionageTechnology')
    elif data.Available_technologies['computerTechnology']:
        research_technology(driver, data, 'computerTechnology')
    elif data.Available_technologies['energyTechnology'] and data.Technologies_levels['energyTechnology'] < 8:
        research_technology(driver, data, 'energyTechnology')
    elif data.Available_technologies['laserTechnology'] and data.Technologies_levels['energyTechnology'] < 12:
        research_technology(driver, data, 'laserTechnology')
    elif data.Available_technologies['combustionDriveTechnology']:
        research_technology(driver, data, 'combustionDriveTechnology')
    elif data.Available_technologies['weaponsTechnology']:
        research_technology(driver, data, 'weaponsTechnology')
    elif data.Available_technologies['armorTechnology']:
        research_technology(driver, data, 'armorTechnology')
    else:
        return True


def research_technology(driver, data, research_name):
    try:
        driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=research')
        driver.find_element(By.CSS_SELECTOR, data.Technologies_upgrade_buttons[research_name]).click()
        print(Fore.BLUE + f'{research_name} research was started')
        print(Style.RESET_ALL)
        data.Factory_available_to_build['researchLaboratory'] = False
    except:
        print(Fore.RED + f'{research_name} facility was NOT built')
        print(Style.RESET_ALL)
