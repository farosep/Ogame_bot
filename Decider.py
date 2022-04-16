#! /usr/bin/env python
# -*- coding: utf-8 -*-


def decide_what_to_do(data):
    if decide_what_to_upgrade(data.Technologies):
        if decide_what_to_upgrade(data.Factories):
            if decide_what_to_upgrade(data.Mines):
                if decide_what_to_upgrade(data.Storages):
                    decide_what_ship_to_build(data.Ships)


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
