import pytest
from selene.support.shared import browser

from mobile_test_demo.assist import attach
from tests.running_session import get_browser_option, run_session, cap


@pytest.fixture(scope="function", autouse=True)
def run_build():
    get_browser_option(browser)
    run_session(cap)
    yield
    attach.add_video(browser)
    browser.quit()
