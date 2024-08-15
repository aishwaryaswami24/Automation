from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir='./videos')
    page=context.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.wait_for_timeout(2000)
    page.screenshot(path='./screenshots/loginpage.png')

    username=page.wait_for_selector('//input[@name="username"]')
    username.fill('Admin')
    password=page.wait_for_selector('//input[@name="password"]')
    password.fill('admin123')
    login=page.wait_for_selector('//button[@type="submit"]')
    login.click()
    page.wait_for_timeout(2000)
    page.screenshot(path='./screenshots/homepage.jpeg')
    page.wait_for_timeout(5000)

    #you need to close context or else your video will not play
    #Videos are saved when the browser context is closed
    #Close the context explicitly, which will ensure that the video is saved properly:

    context.close()
    browser.close()
