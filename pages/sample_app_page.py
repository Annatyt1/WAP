from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class SampleAppPage(BasePage):

    # region Locators
    _sample_app_link = "//a[@href='/sampleapp']"
    _username = "//input[@name='UserName']"
    _password = "//input[@name='Password']"
    _login_button = "login"
    _login_status = "loginstatus"
    # endregion

    @allure.step('step1: click Home page Sample App link')
    def go_to_sample_app_page(self):
        self.click_on(self._sample_app_link)

    def login(self, username, password):

        self.send_text(self._username, username)
        self.send_text(self._password, password)
        self.click_on(find_by=By.ID, locator=self._login_button)

    def verify_login_msg(self):
        elem = self.driver.find_element(By.ID, self._login_status)
        return elem.text
