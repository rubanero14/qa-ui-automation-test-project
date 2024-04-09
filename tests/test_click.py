import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_click(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/click
    Purpose: To select and click a button mimicking a mouse click
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "click")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Selecting target button with id 'badButton'")
    selector = page.locator("[id='badButton']") # Selecting target button

    print("Clicking target button")
    util.click_button(selector)


    # Assert
    print("Asserting target button is visible")
    expect(selector).to_be_visible()

    util.garbage_collection(browser, context)