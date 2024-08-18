from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=500)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username=page.wait_for_selector('//input[@name="username"]')
    username.type('Admin')
    password=page.wait_for_selector('//input[@name="password"]')
    password.type('admin123')
    login=page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(2000)
    browser.close()

