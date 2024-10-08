import pytest
import sys
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page= browser.new_page()
    yield page
    page.close()



@pytest.mark.skipif(sys.platform=='win32',reason='skip if platform version is win32')
def test_site(page):
    page.goto('https://www.amazon.in/')
    page.wait_for_timeout(2000)
    assert page.title() == 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    print(page.title())


@pytest.mark.skip(reason='test is not ready yet')
def test_site1(page):
    page.goto('https://www.instagram.com/')
    page.wait_for_timeout(2000)
    assert page.url == 'https://www.instagram.com/'
    print(page.url)

