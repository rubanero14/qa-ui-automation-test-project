import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_visibility(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/visibility
    Purpose: After 'Hide' button clicked, checking if button visibility based on below criteria;
        - Removed
        - Zero width
        - Overlapped
        - Opacity 0
        - Visibility hidden
        - Display none
        - Offscreen
    """

    # Arrange
    util = Utility() 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "visibility")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector
    hide_button = page.locator("[id='hideButton']")
    removed_button = page.locator("[id='removedButton']")
    zero_width_button = page.locator("[id='zeroWidthButton']")
    overlapped_button = page.locator("[id='overlappedButton']")
    transparent_button = page.locator("[id='transparentButton']")
    invisible_button = page.locator("[id='invisibleButton']")
    not_displayed_button = page.locator("[id='notdisplayedButton']")
    offscreen_button = page.locator("[id='offscreenButton']")

    print("Clicking the hide button")
    util.click_button(hide_button) # Clicking "Hide" button
    

    # Assert
    print(f"Assertion checking all button visibilty before hide button clicked")
    print("Asserting button with id 'removedButton' is hidden")
    expect(removed_button).to_be_hidden()

    print("Asserting button with id 'zeroWidthButton' is hidden")
    expect(zero_width_button).to_be_hidden()

    print("Asserting button with id 'overlappedButton' is visible")
    expect(overlapped_button).to_be_visible()

    print("Asserting button with id 'transparentButton' is visible")
    expect(transparent_button).to_be_visible()

    print("Asserting button with id 'invisibleButton' is hidden")
    expect(invisible_button).to_be_hidden()

    print("Asserting button with id 'notdisplayedButton' is hidden")
    expect(not_displayed_button).to_be_hidden()

    print("Asserting button with id 'offscreenButton' is visible")
    expect(offscreen_button).to_be_visible()

    util.garbage_collection(browser, context)