from pages.your_list_page import YourListPage
from pages.login_page import LoginPage
from pages.shopping_list_page import ShoppingListPage
from pages.recipes_page import RecipePage
from time import sleep


def test_sign_up(driver_not_logged_in):
    sign_up_page = LoginPage(driver_not_logged_in)
    sign_up_page.open_login_page()
    sign_up_page.sign_up()


def test_sign_up_validation_invalid_email(driver_not_logged_in):
    sign_up_validation_invalid_email = LoginPage(driver_not_logged_in)
    sign_up_validation_invalid_email.open_login_page()
    sign_up_validation_invalid_email.sign_up_invalid_email()


def test_sign_up_validation_empty_email(driver_not_logged_in):
    sign_up_validation_invalid_email = LoginPage(driver_not_logged_in)
    sign_up_validation_invalid_email.open_login_page()
    sign_up_validation_invalid_email.sign_up_empty_email()


def test_sign_in_wrong_password_validation(driver_not_logged_in):
    sign_in_password_validation = LoginPage(driver_not_logged_in)
    sign_in_password_validation.open_login_page()
    sign_in_password_validation.sign_in_wrong_password()


def test_sign_in_empty_password_validation(driver_not_logged_in):
    sign_in_password_validation = LoginPage(driver_not_logged_in)
    sign_in_password_validation.open_login_page()
    sign_in_password_validation.sign_in_empty_password()


def test_sign_in(driver_not_logged_in):
    sign_in_page = LoginPage(driver_not_logged_in)
    sign_in_page.open_login_page()
    sign_in_page.sign_in()


def test_reset_password(driver_not_logged_in):
    reset_password = LoginPage(driver_not_logged_in)
    reset_password.open_login_page()
    reset_password.reset_password()


def test_x_adding_shopping_list(driver_logged_in):
    x_adding_shopping_list = YourListPage(driver_logged_in)
    x_adding_shopping_list.open()
    x_adding_shopping_list.add_a_shopping_list()
    x_adding_shopping_list.x_shopping_list()


def test_cancel_adding_shopping_list(driver_logged_in):
    cancel_adding_shopping_list = YourListPage(driver_logged_in)
    cancel_adding_shopping_list.open()
    cancel_adding_shopping_list.add_a_shopping_list()
    cancel_adding_shopping_list.cancel_shopping_list()


def test_adding_shopping_list(driver_logged_in):
    adding_shopping_list = YourListPage(driver_logged_in)
    adding_shopping_list.open()
    adding_shopping_list.add_a_shopping_list()
    adding_shopping_list.inputting_name_shopping_list()
    adding_shopping_list.adding_shopping_list()
    sleep(10)
    adding_shopping_list.is_created_shopping_list_exists()


def test_deleting_first_shopping_list(driver_logged_in):
    deleting_a_shopping_list = ShoppingListPage(driver_logged_in)
    deleting_a_shopping_list.purification_shopping_list()


def test_x_adding_recipe(driver_logged_in):
    x_adding_recipe = YourListPage(driver_logged_in)
    x_adding_recipe.open()
    x_adding_recipe.add_a_recipe()
    x_adding_recipe.x_recipe()


def test_cancel_adding_recipe(driver_logged_in):
    cancel_adding_recipe = YourListPage(driver_logged_in)
    cancel_adding_recipe.open()
    cancel_adding_recipe.add_a_recipe()
    cancel_adding_recipe.cancel_recipe()


def test_adding_recipe(driver_logged_in):
    adding_recipe = YourListPage(driver_logged_in)
    adding_recipe.open()
    adding_recipe.add_a_recipe()
    adding_recipe.inputting_name_recipe()
    adding_recipe.adding_recipe()
    sleep(10)
    adding_recipe.is_created_recipe_exists()


def test_deleting_first_recipe(driver_logged_in):
    deleting_a_recipe = RecipePage(driver_logged_in)
    deleting_a_recipe.purification_recipe()










