import pytest
from selene import browser


def test_github_desktop(setup_screen_resolution):
    if setup_screen_resolution == "mobile":
        pytest.skip(reason="Пропускаем мобильный тест")

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(setup_screen_resolution):
    if setup_screen_resolution == "desktop":
        pytest.skip(reason="Пропускаем десктопный тест")

    browser.open('/')
    browser.element('.js-header-menu-toggle.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
