from selenium.webdriver.common.by import By

class BasePage:

    base_url = 'http://uitestingplayground.com/'

    def __init__(self, driver) -> None:
        self.driver = driver

    def click_on(self, locator, find_by=By.XPATH):
        element = self.driver.find_element(find_by, locator)
        element.click()
        return element

    def send_text(self, locator, text) -> None:
        elem = self.click_on(locator)
        elem.send_keys(text)
