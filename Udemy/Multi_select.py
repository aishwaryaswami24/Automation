from playwright.sync_api import sync_playwright
with (sync_playwright() as p):
    browser=p.chromium.launch(headless=False,slow_mo=500)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    checkbox=page.wait_for_selector('//input[@value="Cricket"]')
    checkbox.check()
    checkbox=page.wait_for_selector('//input[@value="Movies"]')
    checkbox.check()
    checkbox=page.wait_for_selector('//input[@value="Hockey"]')
    checkbox.check()

    #validation test
    if checkbox.is_checked():
        print('Passed')
    else:
        print('Failed')

    page.wait_for_timeout(5000)
    browser.close()