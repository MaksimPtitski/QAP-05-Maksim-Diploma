from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

name_of_shopping_list_1 = 'BAKERY'
name_of_shopping_list_2 = 'Trout'
name_of_recipe_1 = 'PASTA'
first_list = (By.CSS_SELECTOR, '#listDiv>:nth-child(2)')
first_recipe = (By.CSS_SELECTOR, '#listDiv>:nth-child(4)')
login_button = (By.CLASS_NAME, 'login')
add_a_shopping_list_button = (By.ID, 'createListButton')
shopping_list_name_field = (By.ID, 'addListName')
recipe_name_field = (By.ID, 'addListName')
x_button_shopping_list = (By.CSS_SELECTOR, '[title="Close"]')
cancel_button_shopping_list = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(1)')
add_list_button_shopping_list = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(2)')
add_a_recipe_button = (By.ID, 'createRecipeButton')
x_button_recipe_list = (By.CSS_SELECTOR, '[title="Close"]')
cancel_button_recipe_list = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(1)')
add_recipe_button = (By.CSS_SELECTOR, '.ui-dialog-buttonset>:nth-child(2)')
manage_master_list_button = (By.ID, 'manageMasterListButton')
delete_all_items_in_master_list_button = (By.ID, 'purgeMasterListButton')
delete_all_in_master_list_confirmation_button = (By.XPATH, '/html/body/div[9]/div[3]/div/button[2]')
list_in_master_list = (By.CLASS_NAME, 'item')
lists_button = (By.ID, 'backButton')
manage_categories_button = (By.ID, 'manageCategoriesButton')
you_have_no_shopping_list = (By.CSS_SELECTOR, "#listDiv>:nth-child(2)")
you_have_no_recipes = (By.CSS_SELECTOR, "#listDiv>:nth-child(4)")
add_a_category_button = (By.ID, 'addItemButton')
add_a_category_very_bottom_of_list = (By.CSS_SELECTOR, '.item.command-item')
adding_category_name_field = (By.ID, 'addListName')
adding_category_cancel_button = (By.XPATH, '/html/body/div[2]/div[3]/div/button[1]')
adding_category_add_category_button = (By.XPATH, '/html/body/div[2]/div[3]/div/button[2]')
categories_first_element = (By.CSS_SELECTOR, '.ui-widget.ui-sortable>:nth-child(2)')
category_details_name_field = (By.ID, 'categoryName')
delete_category_button = (By.ID, 'deleteCategoryButton')
cancel_button_category_details = (By.XPATH, '/html/body/div[4]/div[3]/div/button[1]')
ok_button_category_details = (By.XPATH, '/html/body/div[4]/div[3]/div/button[2]')
import_items_button = (By.ID, 'importItemsButton')
master_list_field = (By.CSS_SELECTOR, '.item.command-item')
delete_all_items_button = (By.ID, 'purgeMasterListButton')
forget_d_a_d_order = (By.ID, 'purgeSortOrderButton')
add_an_item_button = (By.ID, 'addItemButton')
milk_element_in_list = (By.CSS_SELECTOR, '#addItemMasterList>:nth-child(2)')
milk_element_in_list_text = 'milk'
text_in_empty_master_list = 'The master list is empty. Add an item...'
add_item_dialog_add_button = (By.ID, 'addItemDialogAddButton')


class YourListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.ourgroceries.com/your-lists/')

    def open_sign_in(self):
        self.find_element(login_button).click()
        
    def open_manage_master_list(self):
        self.find_element(manage_master_list_button).click()

    def purge_master_list(self):
        sleep(3)
        self.open()
        self.open_manage_master_list()
        self.find_element(delete_all_items_in_master_list_button).click()
        self.find_element(delete_all_in_master_list_confirmation_button).click()
        sleep(3)
        self.find_element(lists_button).click()

    def is_master_list_purged(self):
        sleep(3)
        assert self.find_element(list_in_master_list).text == text_in_empty_master_list

    def add_a_shopping_list(self):
        self.find_element(add_a_shopping_list_button).click()

    def x_shopping_list(self):
        x_button_element = self.find_element(x_button_shopping_list)
        x_button_element.click()
        assert self.find_element(you_have_no_shopping_list).is_displayed()

    def cancel_shopping_list(self):
        cancel_button_element = self.find_element(cancel_button_shopping_list)
        cancel_button_element.click()
        assert self.find_element(you_have_no_shopping_list).is_displayed()

    def adding_shopping_list(self):
        adding_list_element = self.find_element(add_list_button_shopping_list)
        adding_list_element.click()

    def inputting_name_shopping_list(self, name_of_shopping_list):
        inputting_name_shopping_list_element = self.find_element(shopping_list_name_field)
        inputting_name_shopping_list_element.send_keys(name_of_shopping_list)

    def is_created_shopping_list_exists(self):
        is_created_shopping_list_exists_element = self.find_element(first_list)
        assert is_created_shopping_list_exists_element.text == name_of_shopping_list_1

    def add_a_recipe(self):
        self.find_element(add_a_recipe_button).click()

    def x_recipe(self):
        x_recipe_element = self.find_element(x_button_recipe_list)
        x_recipe_element.click()
        assert self.find_element(you_have_no_recipes).is_displayed()

    def cancel_recipe(self):
        cancel_button_element = self.find_element(cancel_button_recipe_list)
        cancel_button_element.click()
        assert self.find_element(you_have_no_recipes).is_displayed()

    def adding_recipe(self):
        adding_recipe_element = self.find_element(add_recipe_button)
        adding_recipe_element.click()

    def inputting_name_recipe(self, name_of_recipe_1):
        inputting_name_recipe_element = self.find_element(recipe_name_field)
        inputting_name_recipe_element.send_keys(name_of_recipe_1)

    def is_created_recipe_exists(self):
        is_created_recipe_exists_element = self.find_element(first_recipe)
        assert is_created_recipe_exists_element.text == name_of_recipe_1

    def flow_add_shopping_list(self, name_shopping_list):
        self.open()
        self.add_a_shopping_list()
        self.inputting_name_shopping_list(name_shopping_list)
        self.adding_shopping_list()
        sleep(10)
        first_list_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(first_list)
        )
        first_list_element.click()

    def flow_add_item_to_shopping_list(self, item_element, item_name_title):
        add_an_item_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(add_an_item_button)
        )
        add_an_item_button_element.click()
        adding_item_element = self.find_element(item_element)
        adding_item_element.click()
        sleep(10)
        is_created_item_exists_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".value-note>.value"))
        )
        assert item_name_title in is_created_item_exists_element.text

    def flow_add_recipe(self, name_recipe):
        self.open()
        self.add_a_recipe()
        self.inputting_name_recipe(name_recipe)
        self.adding_recipe()
        sleep(10)
        first_list_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(first_recipe)
        )
        first_list_element.click()

    def flow_add_item_to_recipe(self, item_element, item_name_title):
        add_an_item_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(add_an_item_button)
        )
        add_an_item_button_element.click()
        adding_item_element = self.find_element(item_element)
        adding_item_element.click()
        sleep(10)
        is_created_item_exists_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".value-note>.value"))
        )
        assert item_name_title in is_created_item_exists_element.text
