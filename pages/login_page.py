from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE


#email
#password

email_field = (By.NAME, 'emailAddress')
sign_in_button = (By.CLASS_NAME, 'ui-button')
password_first = (By.NAME, 'password')
password_second = (By.NAME, 'passwordAgain')
create_account = (By.NAME, 'action')
authorisation_email_displayed = (By.ID, 'auth-text')
authorisation_email = 'new15@test.com' #change only numbers and make sure it's length is 14 symbols
registration_email = 'new19@test.com' #change only numbers and make sure it's length is 14 symbols
invalid_registration_email = 'wefwefwef'
empty_registration_email = ''
validation_login_error_field = (By.CLASS_NAME, 'error')
validation_message_empty_email_field = 'You didn’t provide an e-mail address. You need to choose one from your family and enter it here and in each mobile version of OurGroceries you use.'
validation_message_wrong_password = 'The password you entered was not correct, please try again. If you’ve forgotten your password, click the “Reset Password” button below.'
validation_message_empty_password = validation_message_wrong_password
reset_password_button = (By.XPATH, '/html/body/div/div[3]/form/div/div[2]/button')
reset_password_text_field = (By.CLASS_NAME, 'notice')
reset_password_email_sent_text = 'An email has been sent to new15@test.com. Please click the link in that email to reset your password.'


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://www.ourgroceries.com/sign-in?url=%2Fyour-lists%2F")

    def sign_up_invalid_email(self):
        email_field_element = self.find_element(email_field)
        email_field_element.send_keys(invalid_registration_email)
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        assert self.is_password_not_field_presented()

    def sign_up_empty_email(self):
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        validation_message = self.find_element(validation_login_error_field)
        assert validation_message.text == validation_message_empty_email_field

    def is_password_not_field_presented(self):
        try:
            password_first_element = self.find_element(password_first)
            password_first_element.send_keys('qwerty')
            return False
        except WDE:
            return True

    def sign_up(self):
        email_field_element = self.find_element(email_field)
        email_field_element.send_keys(registration_email)
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        password_first_element = self.find_element(password_first)
        password_first_element.send_keys('qwerty')
        password_second_element = self.find_element(password_second)
        password_second_element.send_keys('qwerty')
        create_account_element = self.find_element(create_account)
        create_account_element.click()
        authorisation_email_displayed_element = self.find_element(authorisation_email_displayed)
        #print(authorisation_email_displayed_element.text)
        assert len(authorisation_email_displayed_element.text) == 22 + len(registration_email)

    def sign_in(self):
        email_field_element = self.find_element(email_field)
        email_field_element.send_keys(authorisation_email)
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        password_first_element = self.find_element(password_first)
        password_first_element.send_keys('qwerty')
        create_account_element = self.find_element(create_account)
        create_account_element.click()
        authorisation_email_displayed_element = self.find_element(authorisation_email_displayed)
        assert len(authorisation_email_displayed_element.text) == 22 + len(authorisation_email)

    def sign_in_wrong_password(self):
        email_field_element = self.find_element(email_field)
        email_field_element.send_keys(authorisation_email)
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        password_first_element = self.find_element(password_first)
        password_first_element.send_keys('qwert')
        create_account_element = self.find_element(create_account)
        create_account_element.click()
        validation_message = self.find_element(validation_login_error_field)
        assert validation_message.text == validation_message_wrong_password

    def sign_in_empty_password(self):
        email_field_element = self.find_element(email_field)
        email_field_element.send_keys(authorisation_email)
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        #password_first_element = self.find_element(password_first)
        #password_first_element.send_keys('qwert')
        create_account_element = self.find_element(create_account)
        create_account_element.click()
        validation_message = self.find_element(validation_login_error_field)
        assert validation_message.text == validation_message_empty_password

    def reset_password(self):
        email_field_element = self.find_element(email_field)
        email_field_element.send_keys(authorisation_email)
        sign_in_element = self.find_element(sign_in_button)
        sign_in_element.click()
        reset_password_button_element = self.find_element(reset_password_button)
        reset_password_button_element.click()
        reset_text = self.find_element(reset_password_text_field)
        assert reset_text.text == reset_password_email_sent_text









