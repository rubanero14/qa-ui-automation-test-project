import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_text_input(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/textinput
    Purpose: To perform form input action, ie: passing input value, click update button and 
    verifying the text input value with button value for equality
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "textinput")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector
    input_selector = page.locator("[id='newButtonName']")
    btn_selector = page.locator("[id='updatingButton']")    
    test_string = "test input"

    print("Selecting target input with id 'newButtonName'")
    util.click_button(input_selector) # Selecting target input

    print("Filling up target input with 'test input' value")
    input_selector.fill(test_string)

    print("Clicking target button with id 'updatingButton'")
    util.click_button(btn_selector) # Submission


    # Assert
    print(f"Asserting target button has '{test_string}' value")
    expect(btn_selector).to_have_text(test_string)

    util.garbage_collection(browser, context)