import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_scrollbar(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/scrollbars
    Purpose: To select and click a button that needs to be scrolled and discovered on DOM
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "scrollbars")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Selecting target hidden button with id 'hidingButton'")
    btn_selector = page.locator("[id='hidingButton']") # Selecting hidden button

    print("Clicking target button")
    util.click_button(btn_selector)


    # Assert
    print("Asserting target button is focused and clicked on")
    expect(btn_selector).to_be_focused()

    util.garbage_collection(browser, context)