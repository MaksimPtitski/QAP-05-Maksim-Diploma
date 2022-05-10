from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from pages.your_list_page import name_of_recipe_1
from pages.your_list_page import you_have_no_recipes

first_recipe = (By.CSS_SELECTOR, '#listDiv>:nth-child(4)')
delete_recipe_button = (By.ID, 'deleteListButton')
ok_deleting_recipe_button = (By.XPATH, '/html/body/div[7]/div[3]/div/button[2]')
rename_recipe = (By.ID, 'renameListButton')
recipe_name_field = (By.ID, 'addListName')
renamed_recipe_name_field = ' DI MARE'
rename_recipe_approval = (By.XPATH, '/html/body/div[2]/div[3]/div/button[2]')
recipe_name = (By.CLASS_NAME, 'ui-corner-top')
edit_notes_button = (By.ID, 'editNotesButton')
edit_notes_field = (By.XPATH, '/html/body/div[1]/div[3]/div[5]/div[2]/textarea')
edit_note_original_text = 'Everything what you want to add here'
edit_note_edited_text = 'and something more =)'
save_notes_button = (By.ID, 'saveNotesButton')
cancel_notes_button = (By.ID, 'cancelNotesButton')
note_text_displayed = (By.CSS_SELECTOR, '#listNotesView>div')


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
        sleep(5)
        assert self.find_element(you_have_no_recipes).is_displayed()

    def rename_recipe(self):
        rename_recipe_element = self.find_element(rename_recipe)
        rename_recipe_element.click()
        rename_recipe_element = self.find_element(recipe_name_field)
        rename_recipe_element.send_keys(renamed_recipe_name_field)
        rename_recipe_element = self.find_element(rename_recipe_approval)
        rename_recipe_element.click()
        sleep(5)
        rename_recipe_element = self.find_element(recipe_name)
        assert rename_recipe_element.text == name_of_recipe_1 + renamed_recipe_name_field

    def add_notes_recipe(self):
        edit_notes_button_element = self.find_element(edit_notes_button)
        edit_notes_button_element.click()
        edit_notes_text_field_element = self.find_element(edit_notes_field)
        edit_notes_text_field_element.send_keys(edit_note_original_text)
        save_notes_button_element = self.find_element(save_notes_button)
        save_notes_button_element.click()
        sleep(5)
        note_displayed_text_element = self.find_element(note_text_displayed)
        assert note_displayed_text_element.text == edit_note_original_text

    def edit_notes_recipe(self):
        self.add_notes_recipe()
        edit_notes_button_element = self.find_element(edit_notes_button)
        edit_notes_button_element.click()
        edit_notes_text_field_element = self.find_element(edit_notes_field)
        edit_notes_text_field_element.clear()
        edit_notes_text_field_element.send_keys(edit_note_edited_text)
        save_notes_button_element = self.find_element(save_notes_button)
        save_notes_button_element.click()
        sleep(5)
        note_displayed_text_element = self.find_element(note_text_displayed)
        assert note_displayed_text_element.text == edit_note_edited_text

    def cancel_notes_recipe(self):
        self.add_notes_recipe()
        edit_notes_button_element = self.find_element(edit_notes_button)
        edit_notes_button_element.click()
        edit_notes_text_field_element = self.find_element(edit_notes_field)
        edit_notes_text_field_element.clear()
        edit_notes_text_field_element.send_keys(edit_note_edited_text)
        cancel_notes_button_element = self.find_element(cancel_notes_button)
        cancel_notes_button_element.click()
        sleep(5)
        note_displayed_text_element = self.find_element(note_text_displayed)
        assert note_displayed_text_element.text == edit_note_original_text








        # rename_shopping_list_element = self.find_element(rename_list)
        # rename_shopping_list_element.click()
        # rename_shopping_list_element = self.find_element(shopping_list_name_field)
        # rename_shopping_list_element.send_keys(renamed_shopping_list_name_field)
        # rename_shopping_list_element = self.find_element(rename_list_approval)
        # rename_shopping_list_element.click()
        # sleep(5)
        # rename_shopping_list_element = self.find_element(shopping_list_name)
        # #print(rename_shopping_list_element.text)
        # assert rename_shopping_list_element.text == name_of_shopping_list_1 + renamed_shopping_list_name_field