from selene import browser


def test_github_desktop(desktop_screen_resolution):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_screen_resolution):
    browser.open('/')
    browser.element('.js-header-menu-toggle.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
