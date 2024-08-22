from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://playwright.dev/python/')
    page.wait_for_timeout(2000)
    select=page.wait_for_selector('.getStarted_Sjon')
    select.click()
    page.wait_for_timeout(2000)
    browser.close()