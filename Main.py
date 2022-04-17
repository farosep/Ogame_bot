#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import decider
import info_scrapper
from Login import Login
import datetime
from data.main_data import MainData
from data.colony_data import Colony, ColonyData
from selenium.webdriver.common.by import By


class StartGame:
    """
        Base object, to start bot
    """
    def __init__(self) -> None:
        """
            Initialise browser driver and MainData object
        """
        self.driver = webdriver.Firefox()
        self.main_data = MainData(self.driver)
        self.driver.implicitly_wait(3)
        self.login = Login(self.driver, self.main_data)

    def start(self) -> None:
        """
            Starts with login in game,
            then go to infinity circle of getting info and building
        :return: None
        """
        self.login.get_in_account()
        print(
            f"Login complete at time "
            f"({datetime.datetime.now().strftime('%H:%M:%S')})"
        )
        self.get_colonies(self.main_data)
        while True:
            for i in self.main_data.Colonies:
                #  get information
                info_scrapper.get_all_info(
                    self.driver,
                    self.main_data,
                    self.main_data.Colonies[i].colony_data
                )
                #  decide what to build or research
                decider.decide_what_to_do(
                    self.main_data,
                    self.main_data.Colonies[i].colony_data
                )
            if self.driver.current_url == "https://lobby.ogame.gameforge.com/ru_RU/hub":
                self.login.get_in_server()

    def get_colonies(
            self,
            main_data: MainData
    ) -> None:
        """
            Function that add colonies and generate colony_data for all colonies
        :param main_data: Object of MainDataClass
        """
        colonies_list: list = self.driver.find_elements(
            By.XPATH,
            "//*[@id='planetList']//child::div"
        )
        for i in range(len(colonies_list)):
            main_data.Colonies[f"Colony{i + 1}"] = Colony(
                self.driver,
                ColonyData(self.driver, self.main_data)
            )
            main_data.Colonies[f"Colony{i + 1}"].ref = (
                f"//*[@id='planetList']//child::div[{i + 1}]"
            )


a: StartGame = StartGame()
a.start()
