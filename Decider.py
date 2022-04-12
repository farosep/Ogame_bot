from selenium.webdriver.common.by import By
from colorama import Fore, Style


def decide_what_to_do(data):
    if decide_what_mine_to_build(data):
        decide_what_storage_to_build(data)


def build_factory(driver, data, building_name):
    try:
        driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
        driver.find_element(By.CSS_SELECTOR, data.Upgrade_factory_refs[building_name]).click()
        print(Fore.BLUE + f'{building_name} facility  was built')
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + f'{building_name} facility was NOT built')
        print(Style.RESET_ALL)


def decide_what_mine_to_build(data):
    for i in data.Mines:
        if data.Mines[i].try_to_build():
            return False
    return True


def decide_what_storage_to_build(data):
    for i in data.Storages:
        if data.Storages[i].try_to_build():
            return False
    return True

"""
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
"""