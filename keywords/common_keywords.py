from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class CommonKeywords:
    """Common keywords for web automation"""

    def __init__(self):
        self.builtin = BuiltIn()
        self.selenium_lib = None

    def _get_selenium_lib(self):
        """Get SeleniumLibrary instance"""
        if not self.selenium_lib:
            self.selenium_lib = self.builtin.get_library_instance('SeleniumLibrary')
        return self.selenium_lib

    @keyword
    def setup_browser(self, browser="chrome", headless=False):
        """Setup browser with options"""
        selenium_lib = self._get_selenium_lib()

        if browser.lower() == "chrome":
            options = self._get_chrome_options(headless)
            selenium_lib.open_browser(url="about:blank", browser="chrome", options=options)
        elif browser.lower() == "firefox":
            options = self._get_firefox_options(headless)
            selenium_lib.open_browser(url="about:blank", browser="firefox", options=options)
        else:
            selenium_lib.open_browser(url="about:blank", browser=browser)

        selenium_lib.maximize_browser_window()
        selenium_lib.set_selenium_timeout("10s")
        selenium_lib.set_selenium_implicit_wait("5s")

    def _get_chrome_options(self, headless=False):
        """Get Chrome browser options"""
        from selenium.webdriver.chrome.options import Options
        options = Options()

        if headless:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        return options

    def _get_firefox_options(self, headless=False):
        """Get Firefox browser options"""
        from selenium.webdriver.firefox.options import Options
        options = Options()

        if headless:
            options.add_argument("--headless")

        return options

    @keyword
    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        selenium_lib = self._get_selenium_lib()
        try:
            selenium_lib.wait_until_element_is_visible(locator, timeout=f"{timeout}s")
        except TimeoutException:
            self.builtin.fail(f"Element '{locator}' was not visible within {timeout} seconds")

    @keyword
    def wait_for_element_clickable(self, locator, timeout=10):
        """Wait for element to be clickable"""
        selenium_lib = self._get_selenium_lib()
        try:
            selenium_lib.wait_until_element_is_enabled(locator, timeout=f"{timeout}s")
        except TimeoutException:
            self.builtin.fail(f"Element '{locator}' was not clickable within {timeout} seconds")

    @keyword
    def safe_click(self, locator, timeout=10):
        """Safely click element with wait"""
        self.wait_for_element_visible(locator, timeout)
        self.wait_for_element_clickable(locator, timeout)
        self._get_selenium_lib().click_element(locator)

    @keyword
    def safe_input_text(self, locator, text, timeout=10):
        """Safely input text with wait"""
        self.wait_for_element_visible(locator, timeout)
        selenium_lib = self._get_selenium_lib()
        selenium_lib.clear_element_text(locator)
        selenium_lib.input_text(locator, text)

    @keyword
    def take_screenshot_on_failure(self):
        """Take screenshot on test failure"""
        selenium_lib = self._get_selenium_lib()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/failure_{timestamp}.png"
        selenium_lib.capture_page_screenshot(screenshot_path)
        self.builtin.log(f"Screenshot saved: {screenshot_path}")

    @keyword
    def scroll_to_element(self, locator):
        """Scroll to element"""
        selenium_lib = self._get_selenium_lib()
        selenium_lib.scroll_element_into_view(locator)

    @keyword
    def wait_for_page_to_load(self, timeout=30):
        """Wait for page to load completely"""
        selenium_lib = self._get_selenium_lib()
        selenium_lib.wait_for_condition(
            "return document.readyState === 'complete'",
            timeout=f"{timeout}s"
        )

    @keyword
    def verify_element_text_contains(self, locator, expected_text):
        """Verify element text contains expected text"""
        selenium_lib = self._get_selenium_lib()
        actual_text = selenium_lib.get_text(locator)
        if expected_text not in actual_text:
            self.builtin.fail(f"Expected text '{expected_text}' not found in '{actual_text}'")

    @keyword
    def generate_test_data(self, data_type="email"):
        """Generate test data using Faker"""
        from faker import Faker
        fake = Faker()

        data_generators = {
            "email": fake.email,
            "name": fake.name,
            "phone": fake.phone_number,
            "address": fake.address,
            "company": fake.company,
            "text": fake.text,
            "password": lambda: fake.password(length=12, special_chars=True),
        }

        if data_type in data_generators:
            return data_generators[data_type]()
        else:
            return fake.word()
