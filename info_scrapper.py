#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import data.colony_data
import selenium.webdriver


def get_all_info(
        driver: selenium.webdriver.Firefox,
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        Func that use all another get_info functions
    :param driver: webdriver for browser
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    get_mines_info(driver, colony_data)
    get_storages_info(driver, colony_data)
    get_factories_info(driver, colony_data)
    get_technologies_info(driver, colony_data)
    get_ships_info(driver, colony_data)


def get_mines_info(
        driver,
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        Func that get all info about colony mines ( level, available for upgrade etc)
    :param driver: webdriver for browser
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    driver.get(
        "https://s146-ru.ogame.gameforge.com/"
        "game/index.php?page=ingame&component=supplies"
    )
    for i in colony_data.Mines:
        colony_data.Mines[i].get_info()
    print(f"Mines info collected  time ({datetime.datetime.now().strftime('%H:%M:%S')})")


def get_storages_info(
        driver,
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        Func that get all info about colony storages ( capacity, resources income and etc)
    :param driver: webdriver for browser
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    driver.get("https://s146-ru.ogame.gameforge.com/game/index.php?page=resourceSettings")
    for i in colony_data.Storages:
        colony_data.Storages[i].get_resource()
        colony_data.Storages[i].get_resource_income()
        colony_data.Storages[i].get_resource_capacity()
    print(
        f"Storages info collected  time ({datetime.datetime.now().strftime('%H:%M:%S')})"
    )


def get_factories_info(
        driver,
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        Func that get all info about colony factories ( available for upgrade)
    :param driver: webdriver for browser
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    driver.get(
        "https://s146-ru.ogame.gameforge.com/"
        "game/index.php?page=ingame&component=facilities"
    )
    for i in colony_data.Factories:
        colony_data.Factories[i].get_available()

    print(
        f"Factory info collected  time ({datetime.datetime.now().strftime('%H:%M:%S')})"
    )


def get_technologies_info(
        driver,
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        Func that get all info about player technologies( available for upgrade, levels)
    :param driver: webdriver for browser
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    driver.get(
        "https://s146-ru.ogame.gameforge.com/"
        "game/index.php?page=ingame&component=research"
    )
    for i in colony_data.main_data.Technologies:
        colony_data.main_data.Technologies[i].get_info()
    colony_data.Factories["researchLaboratory"].get_available_to_use()
    print(f"Tech info collected  time ({datetime.datetime.now().strftime('%H:%M:%S')})")


def get_ships_info(
        driver,
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        Func that get all info about colony ships ( available for buld, amounts)
    :param driver: webdriver for browser
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    driver.get(
        "https://s146-ru.ogame.gameforge.com/"
        "game/index.php?page=ingame&component=shipyard"
    )
    for i in colony_data.Ships:
        colony_data.Ships[i].get_amount()
        colony_data.Ships[i].get_available()
        colony_data.Ships[i].get_need_amount()
    colony_data.Factories["shipyard"].get_available_to_use()
    print(f"Ships info collected  time ({datetime.datetime.now().strftime('%H:%M:%S')})")
