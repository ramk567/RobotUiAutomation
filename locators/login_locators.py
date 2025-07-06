from .base_locators import BaseLocators

class LoginLocators(BaseLocators):
    """Login page locators"""

    # Login form
    USERNAME_INPUT = "//input[@id='global-login-username']"
    PASSWORD_INPUT = "//input[@id='global-login-password']"
    LOGIN_BUTTON = "//button[@type='submit' or contains(text(), 'Login')]"

    # Login page elements
    LOGIN_FORM = "//form[contains(@class, 'login')]"
    FORGOT_PASSWORD_LINK = "//a[contains(text(), 'Forgot Password')]"
    REMEMBER_ME_CHECKBOX = "//input[@type='checkbox' and contains(@name, 'remember')]"

    # Error messages
    INVALID_CREDENTIALS_ERROR = "//div[contains(text(), 'Invalid credentials')]"
    EMPTY_FIELDS_ERROR = "//div[contains(text(), 'required')]"
