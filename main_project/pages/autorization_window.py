from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_project.base.base_class import Base


class AutorizationWindow(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locaters

    name_input_loc = '//input[@name="user"]'
    password_input_loc = '//input[@name="password"]'
    enter_button_loc = '//*[@id="subbutfrmLg555"]'

    #Getters

    def get_name_input(self):
        return WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, self.name_input_loc)))

    def get_password_input(self):
        return WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, self.password_input_loc)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, self.enter_button_loc)))

    #Actions

    def input_name(self, name):
       self.get_name_input().send_keys(name)

    def input_password(self, password):
        self.get_password_input().send_keys(password)

    def click_enter_button(self):
        self.get_enter_button().click()

    #Metods

    def autorization(self, name_1, password_1):
        self.input_name(name_1)
        self.input_password(password_1)
        self.click_enter_button()


