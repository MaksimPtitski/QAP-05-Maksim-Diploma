import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.your_list_page import YourListPage
from pages.shopping_list_page import ShoppingListPage
from pages.recipes_page import RecipePage
from selenium.webdriver.common.by import By

first_list = (By.CSS_SELECTOR, 'listDiv>:nth-child(2)')


@pytest.fixture(scope='function')
def driver_logged_in():
    service = Service(executable_path='E:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    sign_in_page = LoginPage(driver)
    sign_in_page.open_login_page()
    sign_in_page.sign_in()
    yield driver
    sleep(3)
    driver.quit()


@pytest.fixture(scope='function')
def driver_not_logged_in():
    service = Service(executable_path='E:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    sleep(3)
    driver.quit()


@pytest.fixture(scope='function')
def driver_logged_in_with_purification_shopping_list():
    service = Service(executable_path='E:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    sign_in_page = LoginPage(driver)
    sign_in_page.open_login_page()
    sign_in_page.sign_in()
    yield driver
    driver.get('https://www.ourgroceries.com/your-lists/')
    sleep(3)
    delete_list = ShoppingListPage(driver)
    delete_list.purification_shopping_list()
    sleep(3)
    your_list_page = YourListPage(driver)
    your_list_page.purge_master_list()
    sleep(3)
    driver.quit()


@pytest.fixture(scope='function')
def driver_logged_in_with_purification_recipe():
    service = Service(executable_path='E:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    sign_in_page = LoginPage(driver)
    sign_in_page.open_login_page()
    sign_in_page.sign_in()
    yield driver
    driver.get('https://www.ourgroceries.com/your-lists/')
    sleep(3)
    delete_list = RecipePage(driver)
    delete_list.purification_recipe()
    sleep(3)
    your_list_page = YourListPage(driver)
    your_list_page.purge_master_list()
    sleep(3)
    driver.quit()
