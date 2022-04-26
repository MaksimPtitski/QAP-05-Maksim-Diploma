from pages.base_page import BasePage
from pages.your_list_page import YourListPage
from selenium.webdriver.common.by import By


first_recipe = (By.CSS_SELECTOR, '#listDiv>:nth-child(4)')
delete_recipe_button = (By.ID, 'deleteListButton')
ok_deleting_recipe_button = (By.XPATH, '/html/body/div[7]/div[3]/div/button[2]')


class RecipePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def purification_recipe(self):
        first_list_element = self.find_element(first_recipe)
        first_list_element.click()
        delete_list_button_element = self.find_element(delete_recipe_button)
        delete_list_button_element.click()
        ok_deleting_list_button_element = self.find_element(ok_deleting_recipe_button)
        ok_deleting_list_button_element.click()
