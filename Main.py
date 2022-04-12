from selenium import webdriver
import Decider
import InfoScrapper
from Login import Login
import time
from data import Data
from Mines.Mines import *
from Mines.Storages import *


class StartGame:
    def __init__(self, data):
        self.driver = webdriver.Firefox()
        self.data = data
        self.driver.implicitly_wait(3)
        self.add_mines(self.data)
        self.add_storages(self.data)

    def start(self):
        Login(self.driver, self.data)
        print(f'Залогинились успешно: time ({datetime.datetime.now().strftime("%H:%M:%S")})')
        while True:
            #  собираем информацию
            InfoScrapper.get_all_info(self.driver, self.data)

            Decider.decide_what_to_do(self.data)
            time.sleep(10)

    def add_mines(self, data):
        data.Mines['MetalMine'] = MetalMine(self.driver, self.data)
        data.Mines['CrystalMine'] = CrystallMine(self.driver, self.data)
        data.Mines['DeuteriumMine'] = DeuteriumMine(self.driver, self.data)
        data.Mines['SolarMine'] = SolarMine(self.driver, self.data)

    def add_storages(self, data):
        data.Storages['metalStorage'] = MetalStorage(self.driver, self.data)
        data.Storages['crystalStorage'] = CrystalStorage(self.driver, self.data)
        data.Storages['deuteriumStorage'] = DeuteriumStorage(self.driver, self.data)
        data.Storages['solarStorage'] = SolarStorage(self.driver, self.data)


d = Data()
a = StartGame(d)
a.start()
