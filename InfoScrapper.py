import datetime
from selenium.webdriver.common.by import By
from colorama import Fore, Style


# Получение данных
def get_all_info(driver, data):
    get_mines_info(driver, data)
    get_storages_info(driver, data)
    get_factories_info(driver, data)
    get_techologies_info(driver, data)


def get_mines_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
    for i in data.Mines:
        data.Mines[i].get_info()
    print(f'Mines info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_storages_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=resourceSettings')
    for i in data.Storages:
        data.Storages[i].get_resource()
        data.Storages[i].get_resource_income()
        data.Storages[i].get_resource_capacity()
    print(f'Storages info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_factories_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=facilities')
    for i in data.Factories:
        data.Factories[i].get_available()
    print(f'Factory info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_techologies_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=research')
    for i in data.Technologies:
        data.Technologies[i].get_info()
    print(f'Tech info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')



