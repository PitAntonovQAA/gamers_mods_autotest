from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from main_project.pages.files_page import FilesPage
from main_project.pages.main_page import MainPage
from main_project.pages.autorization_window import AutorizationWindow
from main_project.pages.skyrim_mods_page import SkyrimModsPage
from main_project.pages.mod_page import ModPage
from main_project.pages.google_disk_page import DiskPage
import os


def download_mod():
    options = webdriver.ChromeOptions()
    options.add_argument('--guest')
    path = input('Введите директорию для загрузки файла')
    prefs = {'download.default_directory': path}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('detach', True)
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://gamer-mods.ru/'

    name = input('Введите имя')
    password = input('Введите пароль')

    main_page = MainPage(driver)
    main_page.open(driver, base_url=url)
    print('Открыта страница')

    main_page.open_profil_page()
    autorization_window = AutorizationWindow(driver )
    autorization_window.autorization(name_1=name, password_1=password)
    print('Пройдена авторизация')

    main_page.open_files_page()
    print('Открыта страница с файлами')

    files_page = FilesPage(driver)
    files_page.open_tes_skyrim_AE()
    print('Открыта страница с модами для скайрима')

    skyrim_mods_page = SkyrimModsPage(driver)
    skyrim_mods_page.open_mod_page()
    print('Открыта страница с модом')

    mod_page = ModPage(driver)
    mod_page.download_mod()
    assert mod_page.is_correct_url('https://drive.google.com/file/d/1UVILfdKqCNDcMulGOsBpUvtcBomLSmCS/view') == True
    print('Страница с загрузкой мода открылась')

    disk_page = DiskPage(driver)
    disk_page.download_mod()
    assert len(os.listdir(path)) > 0
    file_name = 'SkyUI_5_2_SE-12604-5-2SE.7z'
    file_path = path + file_name
    assert os.access(file_path, os.F_OK) == True
    print('Файл скачен')
    os.remove(file_path)

if __name__ == '__main__':
    download_mod()
