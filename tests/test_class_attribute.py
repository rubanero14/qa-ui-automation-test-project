import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_class_attribute(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/classattr
    Purpose: To select a button with given class and perform click action
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "classattr")
    
    
    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Selecting and clicking target button with btn-primary class")
    page.locator('[class*="btn-primary"]').click()

    print("Pop up dismissed")
    page.once("dialog", lambda dialog: dialog.accept())


    # Assert
    print("Asserting target button is visible")
    expect(page.locator('[class*="btn-primary"]')).to_be_visible()

    util.garbage_collection(browser, context)