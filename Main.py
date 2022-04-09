from selenium import webdriver
import Builder
import InfoScrapper
from Login import Login
import time
from data import data


class StartGame():
    def __init__(self, data):
        self.driver = webdriver.Firefox()
        self.data = data
        self.driver.implicitly_wait(10)

    def Start(self):
        Login(self.driver)
        while True:
            #  собираем информацию
            InfoScrapper.get_all_info(self.driver, self.data)
            #  делаем действия
            Builder.decide_what_to_build(self.driver, self.data)
            time.sleep(30)


d = data()
a = StartGame(d)
a.Start()
