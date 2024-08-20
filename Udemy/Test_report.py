from playwright.sync_api import sync_playwright

def test_login():


    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=200)
        context=browser.new_context()
        page=context.new_page()
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        page.wait_for_timeout(2000)
        browser.close()
