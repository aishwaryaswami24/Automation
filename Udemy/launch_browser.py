# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False,slow_mo=500)
#     page=browser.new_page()
#     page.goto('https://playwright.dev/python/')
#     page.get_by_role('link',name='Docs').click()
#     print(page.url)
#     page.wait_for_timeout(5000)
#     browser.close()


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=500)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://playwright.dev/python/')
    print("playwright url launched successfully")
    page.wait_for_timeout(5000)
    browser.close()