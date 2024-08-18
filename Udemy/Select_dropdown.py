from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=500)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # select_dropdown=page.wait_for_selector('#Skills')
    # select_dropdown.select_option(label='Android')

    page.select_option('#Skills',label='Analytics')
    page.wait_for_timeout(5000)
    browser.close()
