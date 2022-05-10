from pages.your_list_page import YourListPage
from pages.login_page import LoginPage
from pages.shopping_list_page import ShoppingListPage
from pages.recipes_page import RecipePage
from time import sleep
from pages.your_list_page import name_of_shopping_list_1
from pages.your_list_page import milk_element_in_list
from pages.your_list_page import milk_element_in_list_text
from pages.your_list_page import name_of_recipe_1
import allure


def test_sign_up(driver_not_logged_in):
    with allure.step('Open login page'):
        sign_up_page = LoginPage(driver_not_logged_in)
        sign_up_page.open_login_page()
    with allure.step('Sign up process itself'):
        sign_up_page.sign_up()


def test_sign_up_validation_invalid_email(driver_not_logged_in):
    with allure.step('Open login page'):
        sign_up_validation_invalid_email = LoginPage(driver_not_logged_in)
        sign_up_validation_invalid_email.open_login_page()
    with allure.step('Sign up process with invalid email'):
        sign_up_validation_invalid_email.sign_up_invalid_email()


def test_sign_up_validation_empty_email(driver_not_logged_in):
    with allure.step('Open login page'):
        sign_up_validation_invalid_email = LoginPage(driver_not_logged_in)
        sign_up_validation_invalid_email.open_login_page()
    with allure.step('Sign up process with an empty e-mail'):
        sign_up_validation_invalid_email.sign_up_empty_email()


def test_sign_in_wrong_password_validation(driver_not_logged_in):
    with allure.step('Open login page'):
        sign_in_password_validation = LoginPage(driver_not_logged_in)
        sign_in_password_validation.open_login_page()
    with allure.step('Sign in with wrong password'):
        sign_in_password_validation.sign_in_wrong_password()


def test_sign_in_empty_password_validation(driver_not_logged_in):
    with allure.step('Open login page'):
        sign_in_password_validation = LoginPage(driver_not_logged_in)
        sign_in_password_validation.open_login_page()
    with allure.step('Sign in without filling the password field'):
        sign_in_password_validation.sign_in_empty_password()


def test_sign_in(driver_not_logged_in):
    with allure.step('Open login page'):
        sign_in_page = LoginPage(driver_not_logged_in)
        sign_in_page.open_login_page()
    with allure.step('Sign in'):
        sign_in_page.sign_in()


def test_reset_password(driver_not_logged_in):
    with allure.step('Open login page'):
        reset_password = LoginPage(driver_not_logged_in)
        reset_password.open_login_page()
    with allure.step('Resetting password'):
        reset_password.reset_password()


def test_x_adding_shopping_list(driver_logged_in):
    with allure.step('Open "Your list" page'):
        x_adding_shopping_list = YourListPage(driver_logged_in)
        x_adding_shopping_list.open()
    with allure.step('Starting the process of adding the shopping list'):
        x_adding_shopping_list.add_a_shopping_list()
    with allure.step('Pressing "X" button for aborting the adding shopping list process'):
        x_adding_shopping_list.x_shopping_list()


def test_cancel_adding_shopping_list(driver_logged_in):
    with allure.step('Open "Your list" page'):
        cancel_adding_shopping_list = YourListPage(driver_logged_in)
        cancel_adding_shopping_list.open()
    with allure.step('Starting the process of adding the shopping list'):
        cancel_adding_shopping_list.add_a_shopping_list()
    with allure.step('Pressing "Cancel" button for cancelling the adding shopping list process'):
        cancel_adding_shopping_list.cancel_shopping_list()


def test_adding_shopping_list(driver_logged_in):
    with allure.step('Open "Your list" page'):
        adding_shopping_list = YourListPage(driver_logged_in)
        adding_shopping_list.open()
    with allure.step('Starting the process of adding the shopping list'):
        adding_shopping_list.add_a_shopping_list()
    with allure.step('Naming of a shopping list process'):
        adding_shopping_list.inputting_name_shopping_list(name_of_shopping_list_1)
    with allure.step('Accepting of adding a shopping list'):
        adding_shopping_list.adding_shopping_list()
        sleep(10)
    with allure.step('Checking if the created shopping list is presented in the list'):
        adding_shopping_list.is_created_shopping_list_exists()


def test_deleting_first_shopping_list(driver_logged_in):
    with allure.step('Deleting a shopping list'):
        deleting_a_shopping_list = ShoppingListPage(driver_logged_in)
        deleting_a_shopping_list.purification_shopping_list()


def test_x_adding_recipe(driver_logged_in):
    with allure.step('Opening "Your list" page'):
        x_adding_recipe = YourListPage(driver_logged_in)
        x_adding_recipe.open()
    with allure.step('Starting the process of adding the recipe'):
        x_adding_recipe.add_a_recipe()
    with allure.step('Pressing "X" button for aborting the adding recipe process'):
        x_adding_recipe.x_recipe()


def test_cancel_adding_recipe(driver_logged_in):
    with allure.step('Opening "Your list" page'):
        cancel_adding_recipe = YourListPage(driver_logged_in)
        cancel_adding_recipe.open()
    with allure.step('Starting the process of adding the recipe'):
        cancel_adding_recipe.add_a_recipe()
    with allure.step('Pressing "Cancel" button for aborting the adding recipe process'):
        cancel_adding_recipe.cancel_recipe()


def test_adding_recipe(driver_logged_in):
    with allure.step('Opening "Your list" page'):
        adding_recipe = YourListPage(driver_logged_in)
        adding_recipe.open()
    with allure.step('Starting the process of adding the recipe'):
        adding_recipe.add_a_recipe()
    with allure.step('Naming of a recipe process'):
        adding_recipe.inputting_name_recipe(name_of_recipe_1)
    with allure.step('Confirmation the process of adding the recipe'):
        adding_recipe.adding_recipe()
        sleep(10)
    with allure.step('Checking if the created recipe exists'):
        adding_recipe.is_created_recipe_exists()


def test_deleting_first_recipe(driver_logged_in):
    with allure.step('Deleting of a recipe'):
        deleting_a_recipe = RecipePage(driver_logged_in)
        deleting_a_recipe.purification_recipe()


def test_adding_item_in_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        adding_item_in_shopping_list_element = YourListPage(driver_logged_in_with_purification_shopping_list)
        adding_item_in_shopping_list_element.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Full flow of adding the item to shopping list'):
        adding_item_in_shopping_list_element.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)


def test_adding_item_in_recipe(driver_logged_in_with_purification_recipe):
    with allure.step('Full flow of adding the recipe'):
        adding_item_in_recipe_element = YourListPage(driver_logged_in_with_purification_recipe)
        adding_item_in_recipe_element.flow_add_recipe(name_of_recipe_1)
    with allure.step('Full flow of adding the item to recipe'):
        adding_item_in_recipe_element.flow_add_item_to_recipe(milk_element_in_list, milk_element_in_list_text)


def test_rename_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        add_shopping_list = YourListPage(driver_logged_in_with_purification_shopping_list)
        add_shopping_list.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Renaming of a shopping list process'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.rename_shopping_list()


def test_rename_recipe(driver_logged_in_with_purification_recipe):
    with allure.step('Full flow of adding the recipe'):
        add_recipe = YourListPage(driver_logged_in_with_purification_recipe)
        add_recipe.flow_add_recipe(name_of_recipe_1)
    with allure.step('Renaming of a recipe process'):
        recipe_page = RecipePage(driver_logged_in_with_purification_recipe)
        recipe_page.rename_recipe()


def test_add_notes_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        add_shopping_list = YourListPage(driver_logged_in_with_purification_shopping_list)
        add_shopping_list.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding notes to shopping list'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.add_notes_shopping_list()


def test_edit_notes_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        add_shopping_list = YourListPage(driver_logged_in_with_purification_shopping_list)
        add_shopping_list.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding and editing notes to shopping list'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.edit_notes_shopping_list()


def test_cancel_editing_notes_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        add_shopping_list = YourListPage(driver_logged_in_with_purification_shopping_list)
        add_shopping_list.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Cancelling editing notes process'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.cancel_notes_shopping_list()


def test_add_notes_recipe(driver_logged_in_with_purification_recipe):
    with allure.step('Full flow of adding the recipe'):
        add_recipe = YourListPage(driver_logged_in_with_purification_recipe)
        add_recipe.flow_add_recipe(name_of_recipe_1)
    with allure.step('Adding notes to recipe'):
        recipes_page = RecipePage(driver_logged_in_with_purification_recipe)
        recipes_page.add_notes_recipe()


def test_edit_notes_recipe(driver_logged_in_with_purification_recipe):
    with allure.step('Full flow of adding the recipe'):
        add_recipe = YourListPage(driver_logged_in_with_purification_recipe)
        add_recipe.flow_add_recipe(name_of_recipe_1)
    with allure.step('Adding and editing notes process'):
        recipes_page = RecipePage(driver_logged_in_with_purification_recipe)
        recipes_page.edit_notes_recipe()


def test_cancel_editing_notes_recipe(driver_logged_in_with_purification_recipe):
    with allure.step('Full flow of adding the recipe'):
        add_recipe = YourListPage(driver_logged_in_with_purification_recipe)
        add_recipe.flow_add_recipe(name_of_recipe_1)
    with allure.step('Cancelling adding notes process'):
        recipes_page = RecipePage(driver_logged_in_with_purification_recipe)
        recipes_page.cancel_notes_recipe()


def test_star_item_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        add_shopping_list = YourListPage(driver_logged_in_with_purification_shopping_list)
        add_shopping_list.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding the item to shopping list'):
        add_item_in_shopping_list = YourListPage(driver_logged_in_with_purification_shopping_list)
        add_item_in_shopping_list.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)
    with allure.step('Adding the "Star" to the item process'):
        edit_item_element = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        edit_item_element.edit_item_star_in_shopping_list()


def test_increasing_numbers_of_items(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        your_list_page = YourListPage(driver_logged_in_with_purification_shopping_list)
        your_list_page.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding the item to shopping list'):
        your_list_page.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)
    with allure.step('Increasing the numbers of selected item to "3"'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.edit_item_more_3_in_shopping_list()


def test_decreasing_numbers_of_items(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        your_list_page = YourListPage(driver_logged_in_with_purification_shopping_list)
        your_list_page.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding the item to shopping list'):
        your_list_page.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)
    with allure.step('Increasing the numbers of selected item to "3"'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.edit_item_more_3_in_shopping_list()
    with allure.step('Decreasing the numbers of selected item to "2"'):
        shopping_list_page.edit_item_fewer_2_in_shopping_list()


def test_deleting_item_shopping_list(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        your_list_page = YourListPage(driver_logged_in_with_purification_shopping_list)
        your_list_page.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding the item to shopping list'):
        your_list_page.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)
    with allure.step('Deleting the item from shopping list'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.delete_item_shopping_list()


def test_set_category_to_item(driver_logged_in_with_purification_shopping_list):
    with allure.step('Full flow of adding the shopping list'):
        your_list_page = YourListPage(driver_logged_in_with_purification_shopping_list)
        your_list_page.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding the item to shopping list'):
        your_list_page.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)
    with allure.step('Setting the "Bakery" category to item'):
        shopping_list_page = ShoppingListPage(driver_logged_in_with_purification_shopping_list)
        shopping_list_page.set_bakery_category()


def test_purge_master_list(driver_logged_in):
    with allure.step('Full flow of adding the shopping list'):
        your_list_page = YourListPage(driver_logged_in)
        your_list_page.flow_add_shopping_list(name_of_shopping_list_1)
    with allure.step('Adding the item to shopping list'):
        your_list_page.flow_add_item_to_shopping_list(milk_element_in_list, milk_element_in_list_text)
    with allure.step('Purging the master list'):
        your_list_page.purge_master_list()
        your_list_page.driver.refresh()
    with allure.step('Opening the master list'):
        your_list_page.open_manage_master_list()
    with allure.step('Checking if the master list is empty'):
        your_list_page.is_master_list_purged()
