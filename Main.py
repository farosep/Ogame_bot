from selenium import webdriver
import Decider
import InfoScrapper
from Login import Login
import time
from data import Data
import datetime


class StartGame:
    def __init__(self, data):
        self.driver = webdriver.Firefox()
        self.data = data
        self.driver.implicitly_wait(3)

    def start(self):
        Login(self.driver, self.data)
        print(f'Залогинились успешно: time ({datetime.datetime.now().strftime("%H:%M:%S")})')
        while True:
            #  собираем информацию
            InfoScrapper.get_all_info(self.driver, self.data)
            #  делаем действия
            Decider.decide_what_to_do(self.driver, self.data)
            time.sleep(30)


d = Data()
a = StartGame(d)
a.start()
