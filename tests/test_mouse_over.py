import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from src.utility import Utility

@pytest.mark.utility
def test_mouse_over(playwright: Playwright):
    """
    Link: http://uitestingplayground.com/mouseover
    Purpose: Mimicking mouse interaction by moving mouse over on a target element, click twice and check
    if dynamics of a mouse interaction on DOM are fulfilled, in this event, click count increased by
    twice per click
    """

    # Arrange
    util = Utility()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    util.open_browser(page, "mouseover")

    # Act
    util.debug_mode(page) # to invoke Playwright Inspector
    click_here_link = page.get_by_text('Click me')
    click_counter = page.locator("[id='clickCount']")

    print("Mouse hover the 'Click me' link")
    click_here_link.hover() # Mouse over this element

    print("Clicking first time")
    util.click_button(click_here_link)

    print("Clicking second time")
    util.click_button(click_here_link) # Clicking "Click me" twice

    # Assert
    print("Asserting that click counter element has value of 2")
    expect(click_counter).to_have_text("2")

    util.garbage_collection(browser, context)