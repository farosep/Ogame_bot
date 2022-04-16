#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:
    def __init__(self, driver, data):
        self.driver = driver
        self.data = data

    def get_in_server(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(1)').click()
        self.driver.find_element(By.XPATH,
                            f"//*[text()='{self.data.Server}']//parent::div//following-sibling::div[7]//button").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')

    def get_in_account(self):
        self.driver.get('https://lobby.ogame.gameforge.com/ru_RU/')
        self.driver.find_element(By.CSS_SELECTOR, '.tabsList > li:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div.inputWrap:nth-child(1) > div:nth-child(2) > input:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR,
                            'div.inputWrap:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(self.data.Login)
        self.driver.find_element(By.CSS_SELECTOR,
                                'div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                'div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys(self.data.Password)
        a = self.driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(1)')
        a.click()
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element(a))
        if self.driver.current_url == 'https://lobby.ogame.gameforge.com/ru_RU/hub':
            self.get_in_server()


