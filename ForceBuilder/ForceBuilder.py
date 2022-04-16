from colorama import Fore, Style
from selenium.webdriver.common.by import By
import datetime


class ForceUnit:
    def __init__(self, driver, data):
        self.driver = driver
        self.data = data
        self.amount = 0
        self.amount_ref = ''
        self.name = ''
        self.available = False
        self.build_button = ''
        self.need_amount = 0
        self.cost_in_metal = 0
        self.cost_in_crystal = 0
        self.cost_in_deuterium = 0
        self.resource_hold = 0

    def get_amount(self):
        try:
            self.amount = int(self.driver.find_element(By.CSS_SELECTOR, self.amount_ref).text)
        except:
            self.amount = 0
            print(Fore.RED + f'Не смогли получить количество {self.name} '
                             f'time ({datetime.datetime.now().strftime("%H:%M:%S")})')
            print(Style.RESET_ALL)

    def get_available(self):
        try:
            a = self.driver.find_element(By.CSS_SELECTOR, self.build_button).get_attribute('data-status')
            if a == 'on':
                self.available = True
            else:
                self.available = False
        except:
            self.available = False

    def try_to_build(self):
        if self.available and self.data.Factories['shipyard'].available_to_use and self.need_amount > self.amount:
            try:
                self.driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=shipyard')
                self.driver.find_element(By.CSS_SELECTOR, self.build_button).click()
                self.driver.find_element(By.CSS_SELECTOR, '#build_amount').send_keys(f'{round(self.need_amount - self.amount)}')
                self.driver.find_element(By.CSS_SELECTOR, 'span.tooltip').click()
                return True
            except:
                print(Fore.RED + f'Не смогли построить {self.need_amount} {self.name} '
                                 f'time ({datetime.datetime.now().strftime("%H:%M:%S")})')
                print(Style.RESET_ALL)
        return False

    def get_need_amount(self):
        self.need_amount = (self.data.Storages['metalStorage'].resource_income + self.data.Storages['crystalStorage'].resource_income * 2
        + self.data.Storages['deuteriumStorage'].resource_income * 3) / (self.cost_in_metal + self.cost_in_crystal*2
                                                                         + self.cost_in_deuterium*3)
