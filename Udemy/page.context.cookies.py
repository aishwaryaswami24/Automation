from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.google.com/')
    #show cookies stroed in website
    cookies=page.context.cookies()
    print(cookies)
    print(len(cookies))

    #clear cookies
    page.context.clear_cookies()

    #add cookies
    # new_cookies={
    #     'name':'aish',
    #     'school': 'skncoe'
    # }
    #
    # page.context.add_cookies([new_cookies])

    #take screenshot
    page.screenshot(path='test.png',full_page=True)
    page.wait_for_timeout(2000)
    browser.close()