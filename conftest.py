import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
  
    # Define mobile emulation settings
    chrome_options = Options()
    chrome_options.add_experimental_option('mobileEmulation', {
        'deviceName': 'iPhone X'
    })

    # Initialize WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # Return WebDriver instance to the test
    yield driver

    # Teardown - close the browser after test completion
    driver.quit()
