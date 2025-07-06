class BaseLocators:
    """Base locators for common elements"""

    # Common buttons
    CONTINUE_BUTTON = "//button[@type='submit']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    CANCEL_BUTTON = "//button[contains(text(), 'Cancel')]"
    SAVE_BUTTON = "//button[contains(text(), 'Save')]"
    DELETE_BUTTON = "//button[contains(text(), 'Delete')]"

    # Common form elements
    LOADING_SPINNER = "//div[contains(@class, 'loading') or contains(@class, 'spinner')]"
    ERROR_MESSAGE = "//div[contains(@class, 'error') or contains(@class, 'alert-danger')]"
    SUCCESS_MESSAGE = "//div[contains(@class, 'success') or contains(@class, 'alert-success')]"

    # Navigation
    HEADER = "//header"
    FOOTER = "//footer"
    NAVIGATION = "//nav"

    # Modal
    MODAL = "//div[contains(@class, 'modal')]"
    MODAL_CLOSE = "//button[contains(@class, 'modal-close')]"
