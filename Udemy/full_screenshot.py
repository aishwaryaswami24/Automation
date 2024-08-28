from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.firefox.launch(headless=False)
    context=browser.new_context(record_video_dir='video.mp4')
    page=context.new_page()
    page.goto('https://playwright.dev/python/')
    page.wait_for_timeout(2000)
    page.set_viewport_size({'height': 200,'width': 300})
    page.screenshot(path='playwright.png',full_page=True)
    page.close()
    page.video.save_as('./video1')
    context.close()

    browser.close()