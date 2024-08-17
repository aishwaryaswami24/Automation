from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/')
    page.wait_for_timeout(2000)
    #CSS selector id,class,attribute
    #id shows by #
    #class .
    #attribute tagname[attribute="value"]
    email=page.wait_for_selector('#email')
    email.fill('abc@gmail.com')
    button=page.wait_for_selector('#enterimg')
    button.click()
    page.wait_for_timeout(2000)
    browser.close()
