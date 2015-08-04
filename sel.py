import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://slavpeople.com/")
        # driver.get("http://test.slavpeople.com/page/sign_up")
        # self.assertIn("Python", driver.title)
        # elem = driver.find_elements_by_xpath("/html/body/div[1]/div/a[2]")
        time.sleep(1)
        # elem = driver.find_element_by_class_name("b-link b-register")
        # elem = driver.find_element_by_xpath("/html/body/div[1]/div[5]/a")
        elem = driver.find_element_by_xpath("//*[@id='register']")
        time.sleep(1)
        # elem.send_keys(Keys.RETURN)
        elem.click()
        time.sleep(1)
        input = driver.find_elements_by_xpath('/html/body/form/div/section[1]/div/div/input')
        input[0].send_keys("username")
        time.sleep(1)
        next = driver.find_elements_by_xpath('/html/body/form/div/section[1]/button')
        next[0].click()
        time.sleep(1)
        input = driver.find_elements_by_xpath('/html/body/form/div/section[2]/div/div/div[1]/label')
        input[0].click()
        next = driver.find_elements_by_xpath('/html/body/form/div/section[2]/button')
        next[0].click()
        # 3 slide
        time.sleep(1)
        day = driver.find_elements_by_name('d')
        day[0].send_keys("12")
        time.sleep(1)
        month = driver.find_elements_by_name('m')
        month[0].send_keys("12")
        time.sleep(1)
        year = driver.find_elements_by_name('m')
        year[0].send_keys("12")
        time.sleep(1)
        next_day = driver.find_elements_by_xpath('/html/body/form/div[2]/section[3]/button')
        next_day[0].click()

        # input.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        # print elem
        # try:
        #     element = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By, "myDynamicElement"))
        #     )
        # finally:
        #     driver.quit()

    def tearDown(self):
        # self.driver.close()
        print 'ok'

if __name__ == "__main__":
    unittest.main()