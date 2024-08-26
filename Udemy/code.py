# multiply= lambda x,y:x*y
# print(multiply(3,5))
#
dict1={'a':2,'b':4}
dict2={'c':6,'d':9}
#
dict1.update(dict2)
print(dict1)

result=dict1 | dict2
print(result)

# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser=p.chromium.launch(headless=False,slow_mo=500)
#     context=browser.new_context()
#     page=context.new_page()
#     page.goto('https://playwright.dev/')
#     # page.wait_for_timeout(1000)
#     # page.wait_for_selector('//div[@class="navbar__item dropdown dropdown--hoverable"]').click()
#     #page.wait_for_selector('//a[@role="button"]').click()
#     page.select_option('//a[@href="/python/"]')
#     print('webpage successfully opened')
#     page.wait_for_timeout(5000)
#     browser.close()
#
# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://playwright.dev/")
#     page.get_by_role("button", name="Node.js").click()
#     page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
