from playwright.sync_api import sync_playwright


text_alert=[]
def handle_dialog(dialog):
    message=dialog.message
    text_alert.append(message)
    dialog.accept()

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=500)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(2000)
    page.on('dialog', handle_dialog)
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(2000)
    print(text_alert[0])
    page.wait_for_timeout(2000)
    browser.close()