from pages.base_page import BasePage
from pages.your_list_page import YourListPage
from selenium.webdriver.common.by import By

first_list = (By.CSS_SELECTOR, '#listDiv>:nth-child(2)')
delete_list_button = (By.ID, 'deleteListButton')
cancel_deleting_list_button = (By.XPATH, '/html/body/div[7]/div[3]/div/button[1]')
ok_deleting_list_button = (By.XPATH, '/html/body/div[7]/div[3]/div/button[2]')
lists_button = (By.ID, 'backButton')
manage_categories_button = (By.ID, 'manageCategoriesButton')
import_items_button = (By.ID, 'importItemsButton')
add_an_item_button = (By.ID, 'addItemButton')
shopping_list_field = (By.CLASS_NAME, "item")
edit_notes_button = (By.ID, 'editNotesButton')
email_list = (By.ID, 'emailListButton')
rename_list = (By.ID, 'renameListButton')
print_button = (By.ID, 'printListButton')


class ShoppingListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def purification_shopping_list(self):
        first_list_element = self.find_element(first_list)
        first_list_element.click()
        delete_list_button_element = self.find_element(delete_list_button)
        delete_list_button_element.click()
        ok_deleting_list_button_element = self.find_element(ok_deleting_list_button)
        ok_deleting_list_button_element.click()








