from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=headless,
            args=['--disable-blink-features=AutomationControlled']
        )
        print(f"[INFO] Headless mode is {'ON' if headless else 'OFF'}")

    def new_page(self):
        context = self.browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            )
        )
        # Evadir detección básica de automatización
        context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        return context.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()
