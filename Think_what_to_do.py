from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Получение данных
def get_all_info(driver, data):
    get_user_resources_info(driver, data)
    get_user_mines_level(driver, data)
    get_available_mines_to_build(driver, data)
    get_resource_income_and_storages(driver, data)


def get_user_resources_info(driver, data):
    for i in data.resources_refs:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.ID, data.resources_refs[i])))
            data.resources[i] = int(driver.find_element(By.ID, data.resources_refs[i]).text.replace('.', ''))
        except:
            print(f'Не смогли найти количество ресурсов {data.resources_refs[i]}')
            data.resources[i] = 0


def get_user_mines_level(driver, data):
    for i in data.mine_levels:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, data.mine_level_refs[i])))
            data.mine_levels[i] = int(driver.find_element(By.CSS_SELECTOR,
                                                          data.mine_level_refs[i]).text.replace('.', ''))
        except:
            try:
                data.mine_levels[i] = int(driver.find_element(By.CSS_SELECTOR,
                                                              data.blocked_mine_level_refs[i]).text.replace('.', ''))
            except:
                print(f'Не смогли получить уровень шахты {data.blocked_mine_level_refs[i]}')
                data.mine_levels[i] = 999


def get_available_mines_to_build(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    for i in data.Upgrade_mines_buttons:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, data.Upgrade_mines_buttons[i])))
            driver.find_element(By.CSS_SELECTOR, data.Upgrade_mines_buttons[i])
            data.Mines_available_to_build[i] = True
        except:
            data.Mines_available_to_build[i] = False


def get_resource_income_and_storages(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=resourceSettings')
    #  Тут собираем инком ресурсов
    for i in data.mine_income_refs:
        try:
            data.resources_income[i] = int(
                driver.find_element(By.CSS_SELECTOR, data.mine_income_refs[i]).text.replace('.', ''))
        except:
            print(f'Не смогли получить прирост {data.mine_income_refs[i]}')
            data.mine_income_refs[i] = 0

    #  Тут собираем вместимость хранилищ
    for i in data.resources_storages:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, data.mine_capacity_refs[i])))
            data.resources_storages[i] = int(
                    driver.find_element(By.CSS_SELECTOR, data.mine_capacity_refs[i]).text.replace('.', ''))
        except:
            try:
                data.resources_storages[i] = int(
                    driver.find_element(By.CSS_SELECTOR, data.mine_overexcited_capacity_refs[i]).text.replace('.', ''))
            except:
                print(f'Не смогли получить размер хранилища {data.mine_capacity_refs[i]}')


def build_resource(driver, building):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    driver.find_element(By.CSS_SELECTOR, building).click()


def build_fabric(driver, building):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
    driver.find_element(By.CSS_SELECTOR, building).click()


def decide_what_mine_to_build(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    # условия постройки солнечной станции
    if data.resources['energy'] <= 0 and data.Mines_available_to_build['SolarEnergy_mine']:
        build_resource(driver, data.Upgrade_mines_buttons['SolarEnergy_mine'])
        data.Mines_available_to_build['SolarEnergy_mine'] = False
    #  Условия постройки металлической шахты
    elif (data.resources['energy'] > 0
          and data.mine_levels['metal_mine_level'] <= data.mine_levels['crystal_mine_level'] + 2
          and data.Mines_available_to_build['metal_mine']):
        build_resource(driver, data.Upgrade_mines_buttons['metal_mine'])
        data.Mines_available_to_build['metal_mine'] = False
    #  Условия постройки кристаллической шахты
    elif (data.resources['energy'] > 0
          and data.mine_levels['crystal_mine_level'] < data.mine_levels['deuterium_mine_level'] + 3
          and data.Mines_available_to_build['crystal_mine']):
        build_resource(driver, data.Upgrade_mines_buttons['crystal_mine'])
        data.Mines_available_to_build['crystal_mine'] = False
    #  Условия постройки дейтериевой шахты
    elif (data.resources['energy'] > 0
          and data.mine_levels['deuterium_mine_level'] < data.mine_levels['crystal_mine_level'] - 3
          and data.Mines_available_to_build['deuterium_mine']):
        build_resource(driver, data.Upgrade_mines_buttons['deuterium_mine'])
        data.Mines_available_to_build['deuterium_mine'] = False
    #  Условия постройки хранилища металла
    elif ((data.resources_income['metal_income']*8 > data.resources_storages['metal_storage']
          or data.resources['metal'] > data.resources_storages['metal_storage'])
          and data.Mines_available_to_build['metal_storage']):
        build_resource(driver, data.Upgrade_mines_buttons['metal_storage'])
        data.Mines_available_to_build['metal_storage'] = False
    #  Условия постройки хранилища кристалла
    elif ((data.resources_income['crystal_income']*8 > data.resources_storages['crystal_storage']
           or data.resources['crystal'] > data.resources_storages['crystal_storage'])
          and data.Mines_available_to_build['crystal_storage']):
        build_resource(driver, data.Upgrade_mines_buttons['crystal_storage'])
        data.Mines_available_to_build['crystal_storage'] = False
    #  Условия постройки хранилища дейтерия
    elif ((data.resources_income['deuterium_income']*8 > data.resources_storages['deuterium_storage']
           or data.resources['deuterium'] > data.resources_storages['deuterium_storage']) and
          data.Mines_available_to_build['deuterium_storage']):
        build_resource(driver, data.Upgrade_mines_buttons['deuterium_storage'])
        data.Mines_available_to_build['deuterium_storage'] = False
