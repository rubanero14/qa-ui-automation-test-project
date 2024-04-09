import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_dynamic_id(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/dynamicid
    Purpose: To select and click a button which has dynamic id
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "dynamicid")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Selecting and clicking target button with text 'Button with Dynamic ID'")
    page.get_by_role("button", name="Button with Dynamic ID").click()


    # Assert
    print("Asserting target button is visible")
    expect(page.get_by_role("button", name="Button with Dynamic ID")).to_be_visible()

    util.garbage_collection(browser, context)