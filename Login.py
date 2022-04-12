#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def Login(driver,data):
    driver.get('https://lobby.ogame.gameforge.com/ru_RU/')
    driver.find_element(By.CSS_SELECTOR,
                            '.tabsList > li:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'div.inputWrap:nth-child(1) > div:nth-child(2) > input:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'div.inputWrap:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(data.Login)
    driver.find_element(By.CSS_SELECTOR,
                            'div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR,
                            'div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys(data.Password)
    a = driver.find_element(By.CSS_SELECTOR,
                            'button.button:nth-child(1)')
    a.click()
    WebDriverWait(driver, 5).until(ec.invisibility_of_element(a))
    driver.find_element(By.CSS_SELECTOR,
                        'button.button:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR,
                        "div.rt-td:nth-child(11) > button:nth-child(1)").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=supplies')
