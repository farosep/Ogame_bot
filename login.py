#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.main_data import MainData
import selenium.webdriver


class Login:
    """
        Class to get in game at the beginning, and after disconnect
    """
    def __init__(
            self,
            driver: selenium.webdriver.Firefox,
            main_data: MainData
    ) -> None:
        self.driver = driver
        self.main_data = main_data

    def get_in_server(self) -> None:
        """
            This func gets player from hub to selected server
        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button.button:nth-child(1)"
        ).click()
        self.driver.find_element(
            By.XPATH,
            f"//*[text()='{self.main_data.Server}']//parent::div//"
            f"following-sibling::div[7]//button"
        ).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_in_account(self) -> None:
        """
            This func go to main page,
            write login and password,
            get to hub and to the server
        :return: Nothing
        """
        self.driver.get("https://lobby.ogame.gameforge.com/ru_RU/")
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".tabsList > li:nth-child(1)"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "div.inputWrap:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "div.inputWrap:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
        ).send_keys(self.main_data.Login)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)"
        ).send_keys(self.main_data.Password)
        a = self.driver.find_element(
            By.CSS_SELECTOR,
            "button.button:nth-child(1)"
        )
        a.click()
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element(a))
        if self.driver.current_url == "https://lobby.ogame.gameforge.com/ru_RU/hub":
            self.get_in_server()
