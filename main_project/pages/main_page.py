from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_project.base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators

    profil_button_loc = '//div[@class="header-right"]'
    files_button_loc = '(//a[@href="/load"])[1]'

    #Getters

    def get_profil_button(self):
        return WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, self.profil_button_loc)))

    def get_files_button(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.files_button_loc)))

    #Actions

    def click_profil_button(self):
        self.get_profil_button().click()

    def click_files_page(self):
        self.get_files_button().click()

    #Methods

    def open_profil_page(self):
        self.click_profil_button()

    def open_files_page(self):
        self.click_files_page()




