import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page=browser.new_page()
    yield page
    page.close()


def test_title_google(page):
    page.goto('https://www.google.com/')
    page.wait_for_timeout(2000)
    assert page.title() == 'Google'


def test_title_insta(page):
    page.goto('https://www.instagram.com/')
    page.wait_for_timeout(2000)
    assert page.title() == 'Instagram'

