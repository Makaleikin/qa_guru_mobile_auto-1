import os
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser

from mobile_test_demo.assist import attach


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": f"bs://{os.getenv('APP_ID')}",

        'bstack:options': {
            "projectName": "MobileAutoProject",
            "buildName": "browserstack-build-DEMO",
            "sessionName": "BStack first_test",

            "userName": f"{os.getenv('USER_NAME')}",
            "accessKey": f"{os.getenv('ACCESS_KEY')}"
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield
    attach.add_video(browser)
    browser.quit()
