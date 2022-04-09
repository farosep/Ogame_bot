from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def decide_what_to_build(driver,data):
    if decide_what_fabric_to_build(driver, data):
        decide_what_mine_to_build(driver, data)


def build_resource(driver,data, building_name):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    driver.find_element(By.CSS_SELECTOR, data.Upgrade_mines_buttons[building_name]).click()


def build_fabric(driver, data, building_name):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
    driver.find_element(By.CSS_SELECTOR, data.Upgrade_fabric_refs[building_name]).click()


def decide_what_mine_to_build(driver, data):
    # условия постройки солнечной станции
    if data.resources['energy'] <= 0 and data.Mines_available_to_build['SolarEnergy_mine']:
        build_resource(driver,data, 'SolarEnergy_mine')
    #  Условия постройки металлической шахты
    elif (data.resources['energy'] > 0
          and data.mine_levels['metal_mine_level'] <= data.mine_levels['crystal_mine_level'] + 2
          and data.Mines_available_to_build['metal_mine']):
        build_resource(driver, data, 'metal_mine')
    #  Условия постройки кристаллической шахты
    elif (data.resources['energy'] > 0
          and data.mine_levels['crystal_mine_level'] < data.mine_levels['deuterium_mine_level'] + 3
          and data.Mines_available_to_build['crystal_mine']):
        build_resource(driver, data, 'crystal_mine')
    #  Условия постройки дейтериевой шахты
    elif (data.resources['energy'] > 0
          and data.mine_levels['deuterium_mine_level'] < data.mine_levels['crystal_mine_level'] - 3
          and data.Mines_available_to_build['deuterium_mine']):
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
        build_resource(driver, data,'crystal_storage')
    #  Условия постройки хранилища дейтерия
    elif ((data.resources_income['deuterium_income']*8 > data.resources_storages['deuterium_storage']
           or data.resources['deuterium'] > data.resources_storages['deuterium_storage']) and
          data.Mines_available_to_build['deuterium_storage']):
        build_resource(driver, data, 'deuterium_storage')
    else:
        return False

def decide_what_fabric_to_build(driver, data):
    if data.Fabrics_available_to_build['researchLaboratory']:
        build_fabric(driver, data, 'researchLaboratory')
    elif data.Fabrics_available_to_build['shipyard']:
        build_fabric(driver, data, 'shipyard')
    elif data.Fabrics_available_to_build['roboticsFactory']:
        build_fabric(driver, data, 'roboticsFactory')
    else:
        return False
