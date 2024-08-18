from playwright.sync_api import sync_playwright
with (sync_playwright() as p):
    browser=p.chromium.launch(headless=False,slow_mo=500)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    checkboxes=["#checkbox1","#checkbox2","#checkbox3"]
    for i in checkboxes:
        box=page.wait_for_selector(i)
        box.click()

    #validation test
    if box.is_checked():
        print('Passed')
    else:
        print('Failed')

    page.wait_for_timeout(5000)
    browser.close()