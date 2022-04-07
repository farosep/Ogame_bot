from selenium import webdriver
import Think_what_to_do
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
            Think_what_to_do.get_all_info(self.driver, self.data)
            #  делаем действия
            Think_what_to_do.decide_what_mine_to_build(self.driver, self.data)
            time.sleep(30)


d = data()
a = StartGame(d)
a.Start()
