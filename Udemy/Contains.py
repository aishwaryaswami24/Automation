from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=500)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username=page.wait_for_selector('//label[contains(text(),"Username")]')
    password=page.wait_for_selector('//label[contains(text(),"Password")]')
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(2000)
    browser.close()

#dynamic way to find out xpath e.g aish123,aish12,aish90
#starts-with  //tagname[starts-with(@id,"aish")]
#ends-with   //tagname[ends-with(@id,"")]

#family
#parent //tagname[@id="value"]/parent :: tagname[]
#child //tagname[@id="value"]/child :: tagname[]
#ancestor

#sibling  //tagname[@attribute="value"]//following-sibling :: tagname[2]