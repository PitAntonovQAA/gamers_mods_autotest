from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver


    def open(self, driver, base_url):
        self.driver.get(base_url)
        self.driver.maximize_window()

    def get_current_url(self):
        print(self.driver.current_url)
        return self.driver.current_url

    #Проверка текста
    def is_correct_text(self, text, element):
        text_element = element.text
        if text_element == text:
            return True
        else:
            return False

    #Проверка URL

    def is_correct_url(self, url):
        assert url == self.driver.current_url
        return True

    def do_screenshot(self):
        time = datetime.datetime.now().strftime("%Y.%m.%d. %H.%M.%S")
        screenshot_name = 'screenshot ' + f'{time}' + '.png'
        self.driver.save_screenshot(f'E:\\hren\\OOP stepik project\\main_project\\screen\\{screenshot_name}')
        print('screenshot saved')
