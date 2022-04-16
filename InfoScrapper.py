#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


# Получение данных
def get_all_info(driver, data):
    get_mines_info(driver, data)
    get_storages_info(driver, data)
    get_factories_info(driver, data)
    get_techologies_info(driver, data)
    get_ships_info(driver, data)


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
    data.Factories['researchLaboratory'].get_available_to_use()
    print(f'Tech info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')


def get_ships_info(driver, data):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=shipyard')
    for i in data.Ships:
        data.Ships[i].get_amount()
        data.Ships[i].get_available()
        data.Ships[i].get_need_amount()
    data.Factories['shipyard'].get_available_to_use()
    print(f'Ships info collected  time ({datetime.datetime.now().strftime("%H:%M:%S")})')
