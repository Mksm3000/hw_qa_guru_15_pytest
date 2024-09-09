import pytest
from selene import browser


@pytest.fixture(params=['1920x1080', '1600x900', '1200x800'])
def desktop_screen_resolution(request):
    browser.config.base_url = 'https://github.com'

    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=['320x568', '360x640', '480x800'])
def mobile_screen_resolution(request):
    browser.config.base_url = 'https://github.com'

    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(
    params=['1920x1080', '1600x900', '1200x800', '320x568', '360x640', '480x800'])
def screen_resolution(request):
    browser.config.base_url = 'https://github.com'

    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=['1920x1080', '1200x800', '360x640', '480x800'])
def setup_screen_resolution(request):
    browser.config.base_url = 'https://github.com'

    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height

    if request.param in ['1920x1080', '1200x800']:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
