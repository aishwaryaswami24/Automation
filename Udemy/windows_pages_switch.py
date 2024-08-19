from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_timeout(2000)
    page.wait_for_selector('//a[@target="_blank"]/button').click()
    page.wait_for_timeout(2000)
    total_pages=context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)

    #print tile of parent and child page
    # print(page.title())
    # new_page=total_pages[1]
    # print(new_page.title())
    # page.wait_for_timeout(2000)
    # browser.close()


    #using page.bring_to_front method
    print(page.title())
    new_page=total_pages[1]
    #bring child page to front
    new_page.bring_to_front()
    print(new_page.title())
    new_page.close()
    #bring parent page to front
    page.bring_to_front()
    page.wait_for_timeout(2000)
    browser.close()