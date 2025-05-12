from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_project.base.base_class import Base


class FilesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locaters

    tes_skyrim_AE_loc = '//*[@id="cid150"]'

    #getters
    def get_tes_skyrim_AE(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.tes_skyrim_AE_loc)))
    #Action
    def click_tes_skyrim_AE(self):
        self.get_tes_skyrim_AE().click()

    #Metods

    def open_tes_skyrim_AE(self):
        self.click_tes_skyrim_AE()