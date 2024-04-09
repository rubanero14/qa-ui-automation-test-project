import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_ajax_data(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/ajax
    Purpose: To click on button which loads after ajax request
    """
    
    # Arrange
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util = Utility()
    util.open_browser(page, "ajax")

    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Clicking ajax button")
    util.click_button(page.locator("[id='ajaxButton']"))

    print("Selecting hidden message element")
    selector = page.locator('text=Data loaded with AJAX get request.') # Selecting target element after ajax request done

    print("Clicking message element")
    util.click_button(selector)
    

    # Assert 
    print("Asserting the message element is visible")
    expect(selector).to_be_visible()

    util.garbage_collection(browser, context)