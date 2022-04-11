import datetime
from selenium.webdriver.common.by import By
from colorama import Fore, Style


# Получение данных
def get_all_info(driver, data):
    get_mines_info(driver, data)
    get_factory_info(driver, data)
    get_techologies_info(driver, data)


def get_mines_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    if get_availables(driver, data.Upgrade_mines_buttons, data.Mines_available_to_build):
        get_user_resources_info(driver, data)
        get_levels(driver, data.mine_levels, data.mine_level_refs, data.blocked_mine_level_refs)
        get_resource_income_and_storages(driver, data)
        print(f'Mines Full info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')
    else:
        print(f'Mines only available info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_factory_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
    get_availables(driver, data.Upgrade_factory_refs, data.Factory_available_to_build)
    print(f'Factory info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_techologies_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=research')
    if get_availables(driver, data.Technologies_upgrade_buttons, data.Available_technologies):
        get_levels(driver, data.Technologies_levels, data.Technologies_levels_refs, data.Blocked_technologies_levels_refs)
        print(f'Tech info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')
    else:
        print(f'Tech only available info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_user_resources_info(driver, data):
    for i in data.resources_refs:
        try:
            data.resources[i] = int(driver.find_element(By.ID, data.resources_refs[i]).text.replace('.', ''))
        except:
            print(Fore.RED + f'Не смогли найти количество ресурсов {data.resources_refs[i]}  time ({datetime.datetime.now().strftime("%H:%M:%S")})')
            print(Style.RESET_ALL)
            data.resources[i] = 0


def get_resource_income_and_storages(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=resourceSettings')
    #  Тут собираем инком ресурсов
    for i in data.mine_income_refs:
        try:
            data.resources_income[i] = int(
                driver.find_element(By.CSS_SELECTOR, data.mine_income_refs[i]).text.replace('.', ''))
        except:
            print(Fore.RED + f'Не смогли получить прирост {data.mine_income_refs[i]}')
            print(Style.RESET_ALL)
            data.resources_income[i] = 0

    #  Тут собираем вместимость хранилищ
    for i in data.resources_storages:
        try:
            data.resources_storages[i] = int(
                    driver.find_element(By.CSS_SELECTOR, data.mine_capacity_refs[i]).text.replace('.', ''))
        except:
            try:
                data.resources_storages[i] = int(
                    driver.find_element(By.CSS_SELECTOR, data.mine_overexcited_capacity_refs[i]).text.replace('.', ''))
            except:
                print(Fore.RED + f'Не смогли получить размер хранилища {data.mine_capacity_refs[i]}  time ({datetime.datetime.now().strftime("%H:%M:%S")})')
                print(Style.RESET_ALL)


def get_levels(driver, levels, refs, blocked_refs):
    for i in levels:
        try:
            levels[i] = int(driver.find_element(By.CSS_SELECTOR,
                                                          refs[i]).text.replace('.', ''))
        except:
            try:
                levels[i] = int(driver.find_element(By.CSS_SELECTOR,
                                                    blocked_refs[i]).text.replace('.', ''))
            except:
                print(Fore.RED + f'Не смогли получить уровень {blocked_refs[i]} time ({datetime.datetime.now().strftime("%H:%M:%S")})')
                print(Style.RESET_ALL)


def get_availables(driver, upgrade_buttons, availables):
    any_true = False
    for i in upgrade_buttons:
        try:
            driver.find_element(By.CSS_SELECTOR, upgrade_buttons[i])
            availables[i] = True
        except:
            availables[i] = False
    for i in availables:
        if i is False:
            pass
        else:
            any_true = True
    if any_true:
        return True
    else:
        return False
