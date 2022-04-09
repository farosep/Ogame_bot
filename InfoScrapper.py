from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Получение данных
def get_all_info(driver, data):
    get_mines_info(driver, data)
    get_fabric_info(driver, data)


def get_mines_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    get_user_resources_info(driver, data)
    get_levels(driver, data.mine_levels, data.mine_level_refs, data.blocked_mine_level_refs)
    get_available_buildings(driver, data.Upgrade_mines_buttons, data.Mines_available_to_build)
    get_resource_income_and_storages(driver, data)


def get_fabric_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
    get_levels(driver, data.Fabric_levels, data.Fabric_level_refs, data.Fabric_level_refs)
    get_available_buildings(driver, data.Upgrade_fabric_refs, data.Fabrics_available_to_build)


def get_user_resources_info(driver, data):
    for i in data.resources_refs:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.ID, data.resources_refs[i])))
            data.resources[i] = int(driver.find_element(By.ID, data.resources_refs[i]).text.replace('.', ''))
        except:
            print(f'Не смогли найти количество ресурсов {data.resources_refs[i]}')
            data.resources[i] = 0


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


def get_levels(driver, levels, refs, blocked_refs):
    for i in levels:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, refs[i])))
            levels[i] = int(driver.find_element(By.CSS_SELECTOR,
                                                          refs[i]).text.replace('.', ''))
        except:
            try:
                levels[i] = int(driver.find_element(By.CSS_SELECTOR,
                                                    blocked_refs[i]).text.replace('.', ''))
            except:
                print(f'Не смогли получить уровень {blocked_refs[i]}')


def get_available_buildings(driver, upgrade_buttons, available_buildings):
    for i in upgrade_buttons:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, upgrade_buttons[i])))
            driver.find_element(By.CSS_SELECTOR, upgrade_buttons[i])
            available_buildings[i] = True
        except:
            available_buildings[i] = False
