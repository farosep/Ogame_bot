#! /usr/bin/env python
# -*- coding: utf-8 -*-


def decide_what_to_do(main_data, colony_data):
    if decide_what_to_upgrade(main_data.Technologies):
        if decide_what_to_upgrade(colony_data.Factories):
            if decide_what_to_upgrade(colony_data.Mines):
                if decide_what_to_upgrade(colony_data.Storages):
                    decide_what_ship_to_build(colony_data.Ships)


def decide_what_to_upgrade(dict):
    for i in dict:
        if dict[i].try_to_upgrade():
            return False
    return True


def decide_what_ship_to_build(dict):
    for i in dict:
        if dict[i].try_to_build():
            return False
    return True
