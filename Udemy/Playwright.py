from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://playwright.dev/python/')
    # page.wait_for_timeout(2000)
    # dropdown=page.wait_for_selector('//a[@role="button"]')
    # dropdown.click()
    # dropdown.select_option(label='Node.js')
    page.wait_for_timeout(2000)
    browser.close()