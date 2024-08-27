from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://playwright.dev/python/')
    page.wait_for_timeout(2000)
    page.screenshot(path='playwright.png')
    browser.close()