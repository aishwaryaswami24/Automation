from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=500)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    #page.on('dialog',lambda dialog : dialog.accept())
    page.on('dialog',lambda dialog : dialog.dismiss())
    page.on('dialog',lambda dialog : print(dialog.message))
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(5000)
    browser.close()