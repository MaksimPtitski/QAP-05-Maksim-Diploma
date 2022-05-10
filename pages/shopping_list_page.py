from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.your_list_page import shopping_list_name_field
from pages.your_list_page import name_of_shopping_list_1
from selenium.common.exceptions import NoSuchElementException
from pages.your_list_page import you_have_no_shopping_list

first_list = (By.CSS_SELECTOR, '#listDiv>:nth-child(2)')
delete_list_button = (By.ID, 'deleteListButton')
cancel_deleting_list_button = (By.XPATH, '/html/body/div[7]/div[3]/div/button[1]')
ok_deleting_list_button = (By.XPATH, '/html/body/div[7]/div[3]/div/button[2]')
lists_button = (By.ID, 'backButton')
manage_categories_button = (By.ID, 'manageCategoriesButton')
import_items_button = (By.ID, 'importItemsButton')
add_an_item_button = (By.ID, 'addItemButton')
shopping_list_field = (By.CLASS_NAME, "item")
milk_element_in_list = (By.CSS_SELECTOR, '#addItemMasterList>:nth-child(2)')
add_item_dialog_add_button = (By.ID, 'addItemDialogAddButton')
first_item_in_shopping_list = (By.CSS_SELECTOR, '.value-note>.value')
edit_notes_button = (By.ID, 'editNotesButton')
edit_notes_field = (By.XPATH, '/html/body/div[1]/div[3]/div[5]/div[2]/textarea')
edit_note_original_text = 'Everything what you want to add here'
edit_note_edited_text = 'and something more =)'
save_notes_button = (By.ID, 'saveNotesButton')
cancel_notes_button = (By.ID, 'cancelNotesButton')
note_text_displayed = (By.CSS_SELECTOR, '#listNotesView>div')
email_list = (By.ID, 'emailListButton')
rename_list = (By.ID, 'renameListButton')
print_button = (By.ID, 'printListButton')
renamed_shopping_list_name_field = ' CAKE'
rename_list_approval = (By.XPATH, '/html/body/div[2]/div[3]/div/button[2]')
shopping_list_name = (By.CLASS_NAME, 'ui-corner-top')
first_remembered_item = (By.XPATH, '/html/body/div[11]/div[2]/div/div[3]/div[1]/img')
edit_first_item_in_shopping_list_button = (By.CLASS_NAME, 'edit')
item_details_ok_button = (By.XPATH, '/html/body/div[3]/div[3]/div/button[2]')
star_button = (By.ID, 'starItemButton')
star_icon = (By.CLASS_NAME, 'star-icon')
more_button = (By.ID, 'moreItemButton')
less_button = (By.ID, 'lessItemButton')
open_category_drop_down_list = (By.ID, 'itemCategory')
bakery_category_in_category_drop_down_list = (By.CSS_SELECTOR, '#itemCategory>:nth-child(1)')
delete_item_button = (By.ID, 'deleteItemButton')


class ShoppingListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def verification_if_remembered_item_exists(self):
        add_item_element = self.find_element(add_an_item_button)
        add_item_element.click()
        sleep(3)
        try:
            basket_near_first_item = self.find_element(first_remembered_item)
            basket_near_first_item.click()
        except NoSuchElementException:
            pass
        sleep(3)
        close_dialog_window = self.find_element(add_item_dialog_add_button)
        close_dialog_window.click()

    def purification_shopping_list(self):
        first_list_element = self.find_element(first_list)
        first_list_element.click()
        delete_list_button_element = self.find_element(delete_list_button)
        delete_list_button_element.click()
        ok_deleting_list_button_element = self.find_element(ok_deleting_list_button)
        ok_deleting_list_button_element.click()
        sleep(5)
        assert self.find_element(you_have_no_shopping_list).is_displayed()

    def adding_a_default_item_in_shopping_list_by_button(self):
        first_list_element = self.find_element(first_list)
        first_list_element.click()
        add_an_item_button_element = self.find_element(add_an_item_button)
        add_an_item_button_element.click()
        adding_milk_element = self.find_element(milk_element_in_list)
        adding_milk_element.click()
        add_item_element = self.find_element(add_item_dialog_add_button)
        add_item_element.click()
        is_created_item_exists_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".value-note>.value"))
        )
        assert "milk" in is_created_item_exists_element.text

    def rename_shopping_list(self):
        rename_shopping_list_element = self.find_element(rename_list)
        rename_shopping_list_element.click()
        rename_shopping_list_element = self.find_element(shopping_list_name_field)
        rename_shopping_list_element.send_keys(renamed_shopping_list_name_field)
        rename_shopping_list_element = self.find_element(rename_list_approval)
        rename_shopping_list_element.click()
        sleep(5)
        rename_shopping_list_element = self.find_element(shopping_list_name)
        assert rename_shopping_list_element.text == name_of_shopping_list_1 + renamed_shopping_list_name_field

    def add_notes_shopping_list(self):
        edit_notes_button_element = self.find_element(edit_notes_button)
        edit_notes_button_element.click()
        edit_notes_text_field_element = self.find_element(edit_notes_field)
        edit_notes_text_field_element.send_keys(edit_note_original_text)
        save_notes_button_element = self.find_element(save_notes_button)
        save_notes_button_element.click()
        sleep(5)
        note_displayed_text_element = self.find_element(note_text_displayed)
        assert note_displayed_text_element.text == edit_note_original_text

    def edit_notes_shopping_list(self):
        self.add_notes_shopping_list()
        edit_notes_button_element = self.find_element(edit_notes_button)
        edit_notes_button_element.click()
        edit_notes_text_field_element = self.find_element(edit_notes_field)
        edit_notes_text_field_element.clear()
        edit_notes_text_field_element.send_keys(edit_note_edited_text)
        save_notes_button_element = self.find_element(save_notes_button)
        save_notes_button_element.click()
        sleep(5)
        edited_note_displayed_text_element = self.find_element(note_text_displayed)
        assert edited_note_displayed_text_element.text == edit_note_edited_text

    def cancel_notes_shopping_list(self):
        self.add_notes_shopping_list()
        edit_notes_button_element = self.find_element(edit_notes_button)
        edit_notes_button_element.click()
        edit_notes_text_field_element = self.find_element(edit_notes_field)
        edit_notes_text_field_element.clear()
        edit_notes_text_field_element.send_keys(edit_note_edited_text)
        cancel_notes_button_element = self.find_element(cancel_notes_button)
        cancel_notes_button_element.click()
        sleep(5)
        not_edited_note_displayed_text_element = self.find_element(note_text_displayed)
        assert not_edited_note_displayed_text_element.text == edit_note_original_text

    def edit_item_star_in_shopping_list(self):
        edit_first_item_button = self.find_element(edit_first_item_in_shopping_list_button)
        edit_first_item_button.click()
        star_button_element = self.find_element(star_button)
        star_button_element.click()
        ok_item_details_button = self.find_element(item_details_ok_button)
        ok_item_details_button.click()
        sleep(3)
        star_icon_element_exists = self.find_element(star_icon)
        assert star_icon_element_exists.is_displayed()

    def edit_item_more_3_in_shopping_list(self):
        edit_first_item_button = self.find_element(edit_first_item_in_shopping_list_button)
        edit_first_item_button.click()
        more_button_element = self.find_element(more_button)
        more_button_element.click()
        more_button_element.click()
        ok_item_details_button = self.find_element(item_details_ok_button)
        ok_item_details_button.click()
        sleep(10)
        icon_three_element_exists = self.find_element(first_item_in_shopping_list)
        assert "(3)" in icon_three_element_exists.text

    def edit_item_fewer_2_in_shopping_list(self):
        edit_first_item_button = self.find_element(edit_first_item_in_shopping_list_button)
        edit_first_item_button.click()
        less_button_element = self.find_element(less_button)
        less_button_element.click()
        ok_item_details_button = self.find_element(item_details_ok_button)
        ok_item_details_button.click()
        sleep(10)
        icon_three_element_exists = self.find_element(first_item_in_shopping_list)
        assert "(2)" in icon_three_element_exists.text

    def delete_item_shopping_list(self):
        sleep(10)
        edit_first_item_button = self.find_element(edit_first_item_in_shopping_list_button)
        edit_first_item_button.click()
        delete_item_button_element = self.find_element(delete_item_button)
        delete_item_button_element.click()
        sleep(5)
        try:
            self.find_element(first_item_in_shopping_list).is_displayed()
            assert False
        except NoSuchElementException:
            assert True

    def set_bakery_category(self):
        edit_first_item_button = self.find_element(edit_first_item_in_shopping_list_button)
        edit_first_item_button.click()
        category_drop_down_element = self.find_element(open_category_drop_down_list)
        category_drop_down_element.click()
        bakery_element = self.find_element(bakery_category_in_category_drop_down_list)
        bakery_element.click()
        ok_item_details_button = self.find_element(item_details_ok_button)
        ok_item_details_button.click()
        sleep(10)
        edit_first_item_button = self.find_element(edit_first_item_in_shopping_list_button)
        edit_first_item_button.click()
        category_drop_down_element = self.find_element(open_category_drop_down_list)
        assert "Bakery" in category_drop_down_element.text
