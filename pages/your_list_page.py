from pages.base_page import BasePage
from selenium.webdriver.common.by import By

#name_of_a_shopping list
first_list = (By.CSS_SELECTOR, '#listDiv>:nth-child(2)')
first_recipe = (By.CSS_SELECTOR, '#listDiv>:nth-child(4)')
login_button = (By.CLASS_NAME, 'login')
add_a_shopping_list_button = (By.ID, 'createListButton')
shopping_list_name_field = (By.ID, 'addListName')
x_button_shopping_list = (By.CSS_SELECTOR, '[title="Close"]')
cancel_button_shopping_list = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(1)')
add_list_button_shopping_list = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(2)')
add_a_recipe_button =(By.ID, 'createRecipeButton')
recipe_name_field = (By.ID, 'addListName')
x_button_recipe_list = (By.CSS_SELECTOR, '[title="Close"]')
cancel_button_recipe_list = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(1)') #перепроверить
add_recipe_button = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(2)') #перепроверить
manage_master_list_button = (By.ID, 'manageMasterListButton')
lists_button = (By.ID, 'backButton')
manage_categories_button = (By.ID, 'manageCategoriesButton')

add_a_category_button = (By.ID, 'addItemButton') #add category flow
add_a_category_very_bottom_of_list = (By.CSS_SELECTOR, '.item.command-item')
adding_category_name_field = (By.ID, 'addListName')
adding_category_cancel_button = (By.XPATH, '/html/body/div[2]/div[3]/div/button[1]')
adding_category_add_category_button = (By.XPATH, '/html/body/div[2]/div[3]/div/button[2]')

categories_first_element = (By.CSS_SELECTOR, '.ui-widget.ui-sortable>:nth-child(2)') #edit category flow
category_details_name_field = (By.ID, 'categoryName')
delete_category_button = (By.ID, 'deleteCategoryButton')
cancel_button_category_details = (By.XPATH, '/html/body/div[4]/div[3]/div/button[1]')
ok_button_category_details = (By.XPATH, '/html/body/div[4]/div[3]/div/button[2]')

import_items_button = (By.ID, 'importItemsButton') #добавить селекторы для импорта

master_list_field = (By.CSS_SELECTOR, '.item.command-item')
delete_all_items_button = (By.ID, 'purgeMasterListButton')
forget_d_a_d_order = (By.ID, 'purgeSortOrderButton')


class YourListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.ourgroceries.com/your-lists/')

    def open_sign_in(self):
        self.find_element(login_button).click()

    def add_a_shopping_list(self):
        self.find_element(add_a_shopping_list_button).click()

    def x_shopping_list(self):
        x_button_element = self.find_element(x_button_shopping_list)
        x_button_element.click()

    def cancel_shopping_list(self):
        cancel_button_element = self.find_element(cancel_button_shopping_list)
        cancel_button_element.click()

    def adding_shopping_list(self):
        adding_list_element = self.find_element(add_list_button_shopping_list)
        adding_list_element.click()

    def inputting_name_shopping_list(self):
        inputting_name_shopping_list_element = self.find_element(shopping_list_name_field)
        inputting_name_shopping_list_element.send_keys("Trout")

    def is_created_shopping_list_exists(self):
        is_created_shopping_list_exists_element = self.find_element(first_list)
        #print(checking_shopping_list_is_exists_element.text)
        assert is_created_shopping_list_exists_element.text == "Trout"
        #assert adding_shopping_list.is_element_displayed(first_list, "Trout")

    def add_a_recipe(self):
        self.find_element(add_a_recipe_button).click()

    def x_recipe(self):
        x_recipe_element = self.find_element(x_button_recipe_list)
        x_recipe_element.click()

    def cancel_recipe(self):
        cancel_button_element = self.find_element(cancel_button_recipe_list)
        cancel_button_element.click()

    def adding_recipe(self):
        adding_recipe_element = self.find_element(add_recipe_button)
        adding_recipe_element.click()

    def inputting_name_recipe(self):
        inputting_name_recipe_element = self.find_element(recipe_name_field)
        inputting_name_recipe_element.send_keys("Cesar")

    def is_created_recipe_exists(self):
        is_created_recipe_exists_element = self.find_element(first_recipe)
        assert is_created_recipe_exists_element.text == "Cesar"









    #def is_list_contains_correct_name(self):


    #def ?
