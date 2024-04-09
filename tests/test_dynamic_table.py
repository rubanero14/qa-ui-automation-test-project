import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

# @pytest.mark.utility
def test_dynamic_table(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/dynamictable
    Purpose: To select and get value of dynamic table cell and compare its values with reference element
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "dynamictable")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector
    cell_selector = page.locator(":scope", has_text="Chrome").get_by_text("%") # Scoping to the Chrome CPU value
    # wip


    # Assert
    
    util.garbage_collection(browser, context)