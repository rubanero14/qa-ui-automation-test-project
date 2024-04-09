class Utility:
    domain = "http://uitestingplayground.com/"
    def __init__(self):
        self.url = self.domain
        self.click_attempts = 0

        # Debug config: 1 => On debug mode, 0 => Off debug mode 
        self._debug_mode = 0
    
    def get_url(self, path = "") -> str:
        return self.url + path
    
    def get_click_count(self) -> int:
        return self.click_attempts
    
    def click_button(self, selector, timeout = 0) -> None:
        self.click_attempts += 1
        selector.click(timeout = timeout)
    
    def debug_mode(self, page):
        if self._debug_mode == 1:
            print("Playwright Inspector invoked...")
            return page.pause()
        return
    
    def garbage_collection(self, browser, context):
        print("Test PASSED ✅")
        # ---------------------
        context.close()
        browser.close()

    def open_browser(self, page, path) -> None:
        page.goto(self.get_url(path))

    
    