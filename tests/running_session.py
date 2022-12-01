import os
from threading import Thread

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions

BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "artem_12mcWE"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "W7zboLhqDhUMp265cvki"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-DEMO"
capabilities = [
    {
        "browserName": "android",
        "deviceName": "Google Pixel 3",
        "osVersion": "10.0",
        "sessionName": "AndroidTest",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    if "deviceName" in cap:
        bstack_options['deviceName'] = cap["deviceName"]
    if cap['browserName'] in ['ios']:
        cap['browserName'] = 'safari'
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    if cap['browserName'].lower() == 'samsung':
        options.set_capability('browserName', 'samsung')
    browser.config.driver = webdriver.Remote(
        command_executor=URL,
        options=options)


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()