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
            if self.driver.find_element(By.CSS_SELECTOR, self.build_button).get_attribute('data-status') == 'on':
                self.available = True
            self.available = False
        except:
            self.available = False

    def try_to_build(self):
        if self.available:
            try:
                self.driver.get('https://s146-ru.ogame.gameforge.com/game/index.php?page=ingame&component=shipyard')
                self.driver.find_element(By.CSS_SELECTOR, self.build_button).click()
                self.driver.find_element(By.CSS_SELECTOR, '#build_amount').send_keys(self.need_amount)
                self.driver.find_element(By.CSS_SELECTOR, self.build_button).click('span.tooltip')
            except:
                print(Fore.RED + f'Не смогли построить {self.need_amount} {self.name} '
                                 f'time ({datetime.datetime.now().strftime("%H:%M:%S")})')
                print(Style.RESET_ALL)

    def get_need_amount(self):
        self.data.Storages['metalStorage'].resource_income
        self.data.Storages['metalStorage'].resource_income
        self.data.Storages['metalStorage'].resource_income