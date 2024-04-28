import allure
import pytest
from pages.sample_app_page import SampleAppPage

@allure.title('login')
@allure.description('check App can login')
@pytest.mark.parametrize(
    'username,password,expected',
    [
        ('test', 'pwd', 'Welcome, test!'), 
        ('', 'pwd', 'Invalid username/password'), 
        ('test', 'wrong', 'Invalid username/password')],)
def test_sample_app_function_success(driver, username, password, expected):
    # driver = webdriver.Chrome()   # chromedrive
    page = SampleAppPage(driver=driver)
    driver.get(page.base_url)
    page.go_to_sample_app_page()
    page.login(username, password)
    msg = page.verify_login_msg()
    assert msg == expected
