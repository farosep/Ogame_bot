#! /usr/bin/env python
# -*- coding: utf-8 -*-
import data.colony_data


def decide_what_to_do(
        colony_data: data.colony_data.ColonyData
) -> None:
    """
        This func check what it can build / research and do it
    :param colony_data: ColonyData class object
    :return: Nothing
    """
    if decide_what_to_upgrade(colony_data.main_data.Technologies):
        if decide_what_to_upgrade(colony_data.Factories):
            if decide_what_to_upgrade(colony_data.Mines):
                if decide_what_to_upgrade(colony_data.Storages):
                    decide_what_ship_to_build(colony_data.Ships)


def decide_what_to_upgrade(
        dictionary: dict
) -> bool:
    """
        This func for upgrade buildings
    :param dictionary: dict with buildings
    :return: Bool
    """
    for i in dictionary:
        if dictionary[i].try_to_upgrade():
            return False
    return True


def decide_what_ship_to_build(
        dictionary: dict
) -> bool:
    """
        This func for build ships
    :param dictionary: dict with ships
    :return: Bool
    """
    for i in dictionary:
        if dictionary[i].try_to_build():
            return False
    return True
