import pytest
from selene import browser

only_desktop = pytest.mark.parametrize('screen_resolution',
                                       ['1920x1080', '1600x900', '1200x800'],
                                       indirect=True)

only_mobile = pytest.mark.parametrize('screen_resolution',
                                      ['320x568', '360x640', '480x800'],
                                      indirect=True)


@only_desktop
def test_github_desktop(screen_resolution):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@only_mobile
def test_github_mobile(screen_resolution):
    browser.open('/')
    browser.element('.js-header-menu-toggle.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
