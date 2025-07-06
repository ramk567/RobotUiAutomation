from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from keywords.common_keywords import CommonKeywords

class BasePage:
    """Base page class with common functionality"""

    def __init__(self):
        self.builtin = BuiltIn()
        self.common = CommonKeywords()

    @keyword
    def navigate_to(self, url):
        """Navigate to URL"""
        selenium_lib = self.common._get_selenium_lib()
        selenium_lib.go_to(url)
        self.common.wait_for_page_to_load()

    @keyword
    def verify_page_title(self, expected_title):
        """Verify page title"""
        selenium_lib = self.common._get_selenium_lib()
        actual_title = selenium_lib.get_title()
        if expected_title not in actual_title:
            self.builtin.fail(f"Expected title '{expected_title}' not found in '{actual_title}'")

    @keyword
    def verify_url_contains(self, expected_url_part):
        """Verify URL contains expected part"""
        selenium_lib = self.common._get_selenium_lib()
        current_url = selenium_lib.get_location()
        if expected_url_part not in current_url:
            self.builtin.fail(f"Expected URL part '{expected_url_part}' not found in '{current_url}'")

    @keyword
    def wait_for_element_and_click(self, locator, timeout=10):
        """Wait for element and click"""
        self.common.safe_click(locator, timeout)

    @keyword
    def wait_for_element_and_input(self, locator, text, timeout=10):
        """Wait for element and input text"""
        self.common.safe_input_text(locator, text, timeout)
