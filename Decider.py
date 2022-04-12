from selenium.webdriver.common.by import By
from colorama import Fore, Style


def decide_what_to_do(data):
    if decide_what_tech_to_research(data):
        if decide_what_factory_to_build(data):
            if decide_what_mine_to_build(data):
                decide_what_storage_to_build(data)


def decide_what_factory_to_build(data):
    for i in data.Factories:
        if data.Factories[i].try_to_upgrade():
            return False
    return True


def decide_what_mine_to_build(data):
    for i in data.Mines:
        if data.Mines[i].try_to_upgrade():
            return False
    return True


def decide_what_storage_to_build(data):
    for i in data.Storages:
        if data.Storages[i].try_to_upgrade():
            return False
    return True


def decide_what_tech_to_research(data):
    for i in data.Technologies:
        if data.Technologies[i].try_to_upgrade():
            return False
    return True

