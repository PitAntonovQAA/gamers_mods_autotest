from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_project.base.base_class import Base


class SkyrimModsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locaters
    download_filter_button = '(//a[@class="catSortLink"])[4]'
    mod_button_loc  = '//*[@id="entryID4756"]'

    #Getters

    def get_download_filter(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.download_filter_button)))

    def get_mod_button(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.mod_button_loc)))

    #Actions

    def click_download_filter(self):
        self.get_download_filter().click()

    def click_mod_button(self):
        self.get_mod_button().click()

    #Methods

    def open_mod_page(self):
        self.click_download_filter()
        self.click_mod_button()



