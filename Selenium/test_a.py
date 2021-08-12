# from selenium import webdriver
import pytest

def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0

# class TestSample():
#     @pytest.fixture()
#     def test_setup(self):
#         global driver
#         driver = webdriver.Chrome(executable_path="D:\Documents\Selenium\chromedriver.exe")
#         driver.implicitly_wait(10)
#         driver.maximize_window()
#         yield
#         driver.close()
#         driver.quit()
#         print("Test completed")
#
#     def test_login(self,test_setup):
#         driver.get("http://opensource-demo.orangehrmlive.com/")
#         driver.find_element_by_id("txtUsername").send_keys("Admin")
#         driver.find_element_by_id("txtPassword").send_keys("admin123")
#         driver.find_element_by_id("btnLogin").click()
#         x = driver.title
#         assert x == "OrangeHRM"
#     def test_teardown():
#         driver.close()
#         driver.quit()
#         print("Test completed")

