from selenium.webdriver.common.by import By


def get_best_system_position(driver):
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=galaxy')
    pull = driver.find_elements(By.XPATH,
                            '//*[@class="galaxyRow ctContentRow empty_filter"]//div[@class="galaxyCell cellPosition"]')
    best_pos = 15
    for i in pull:
        cur_pos = int(i.text)
        if abs(cur_pos - 8) < best_pos:
            best_pos = cur_pos
    return best_pos

def colonyse_planet(driver):
    pos = get_best_system_position(driver)
    driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=fleetdispatch')
    driver.find_element(By.CSS_SELECTOR, 'li.colonyShip').click()
    driver.find_element(By.CSS_SELECTOR, '#continueToFleet2').click()
    driver.find_element(By.CSS_SELECTOR, '#position').send_keys(f'{pos}')
    driver.find_element(By.CSS_SELECTOR, '#button7').click()
    driver.find_element(By.CSS_SELECTOR, '#sendFleet').click()

