import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_project.base.base_class import Base


class DiskPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    download_button_loc = '//div[@class="ndfHFb-c4YZDc-to915-LgbsSe ndfHFb-c4YZDc-C7uZwb-LgbsSe VIpgJd-TzA9Ye-eEGnhe ndfHFb-c4YZDc-LgbsSe ndfHFb-c4YZDc-C7uZwb-LgbsSe-SfQLQb-Bz112c"]'

    #Gettrs
    def get_download_button(self):
           return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.download_button_loc)))

    #Actions

    def click_download_button(self):
        self.get_download_button().click()

    #Methodds

    def download_mod(self):
        self.click_download_button()
        time.sleep(10)