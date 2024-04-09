import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_hidden_layers(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/loaddelay
    Purpose: To select and click a button after a page loads after delay
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "loaddelay")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector
    page.wait_for_load_state('domcontentloaded')

    print("Selecting target hidden button with text 'Button Appearing After Delay'")
    selector = page.locator("text='Button Appearing After Delay'") # Selecting hidden button

    print("Clicking target button")
    util.click_button(selector)

    # Assert
    print("Asserting target button is visible")
    expect(selector).to_be_visible()

    util.garbage_collection(browser, context)