import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_client_side_delay(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/clientdelays
    Purpose: To select and click an element which appears after client side script process finishes
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "clientdelay")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Selecting and clicking target button with id 'ajaxButton'")
    util.click_button(page.locator("[id='ajaxButton']")) # Selecting target button

    print("Selecting target hidden message element")
    selector = page.locator('text=Data calculated on the client side.')

    print("Clicking the target hidden message element after it appears in the DOM")
    util.click_button(selector) # Selecting target element after it appears on DOM


    # Assert
    print("Asserting target message element is visible")
    expect(selector).to_be_visible()

    util.garbage_collection(browser, context)