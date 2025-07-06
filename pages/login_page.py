from robot.api.deco import keyword
from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    """Login page class"""

    def __init__(self):
        super().__init__()
        self.locators = LoginLocators()

    @keyword
    def enter_username(self, username):
        """Enter username"""
        self.wait_for_element_and_input(self.locators.USERNAME_INPUT, username)

    @keyword
    def enter_password(self, password):
        """Enter password"""
        self.wait_for_element_and_input(self.locators.PASSWORD_INPUT, password)

    @keyword
    def click_login_button(self):
        """Click login button"""
        self.wait_for_element_and_click(self.locators.LOGIN_BUTTON)

    @keyword
    def login_with_credentials(self, username, password):
        """Login with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @keyword
    def verify_login_form_visible(self):
        """Verify login form is visible"""
        self.common.wait_for_element_visible(self.locators.LOGIN_FORM)

    @keyword
    def verify_error_message_displayed(self):
        """Verify error message is displayed"""
        self.common.wait_for_element_visible(self.locators.INVALID_CREDENTIALS_ERROR)
