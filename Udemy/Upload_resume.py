from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.instahyre.com/candidate/profile/')
    upload_file='./Software_Engineer_SDET_Resume_21Aug.pdf'
    upload_location=page.wait_for_selector('//label[@class="edit-link"]/i')
    upload_location.click()
    upload_location.set_input_files(upload_file)
    page.wait_for_timeout(2000)
    browser.close()