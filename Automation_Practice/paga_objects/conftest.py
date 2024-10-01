import pytest
import time
from selenium import webdriver
# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    browser = "chrome"
    if browser.lower() == "chrome":

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://demoqa.com")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    request.cls.driver = driver
    # pytest.driver = driver
    # yield driver
