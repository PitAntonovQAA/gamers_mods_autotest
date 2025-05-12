from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_project.base.base_class import Base


class ModPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locaters
    files_button_loc = '//label[@for="tab2"]'
    mod_download_link_loc = '//*[@id="content2"]/div/div[1]/div[2]/a'

    #Getters
    def get_files_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.files_button_loc)))

    def get_mod_download_link(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.mod_download_link_loc)))

    #Actions

    def click_files_button(self):
        self.get_files_button().click()

    def click_mod_download_link(self):
        self.get_mod_download_link().click()

    #Methods

    def download_mod(self):
        self.click_files_button()
        self.click_mod_download_link()

