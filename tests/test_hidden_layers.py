import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_hidden_layers(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/hiddenlayers
    Purpose: To select and click a button and ensuring it not clicked more than once
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "hiddenlayers")


    # Act
    util.debug_mode(page) # to invoke Playwright Inspector

    print("Selecting target button with id 'greenButton'")
    selector = page.locator("[id='greenButton']")
    
    
    # Assert
    print("Asserting target button is visible")
    expect(selector).to_be_visible()
    
    # Ensuring button only clicked once
    if util.get_click_count() < 1: 
        print(f"Clicking target button {util.get_click_count()} times")
        util.click_button(selector) 
    
    print("Asserting click count >= 1 times")
    assert util.get_click_count() >= 1

    util.garbage_collection(browser, context)