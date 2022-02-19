# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.kazidomi.com/en-FR/shop")
        driver.find_element_by_id("search_query_top").click()
        driver.find_element_by_id("search_query_top").clear()
        driver.find_element_by_id("search_query_top").send_keys("juice")
        driver.find_element_by_id("search_query_top").send_keys(Keys.ENTER)
        try:
            first_juice = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hits']/ul/li[2]/article/div[5]/div")))
            first_juice.get_attribute("data-cart-form-add-product-id")
        finally:
            first_juice = driver.find_element_by_xpath("//*[@id='hits']/ul/li[2]/article/div[5]/div")
            first_juice.click()
            #WebDriverWait(driver, 20).until(
                #EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/a/span[2]")))
        time.sleep(4)
        #first_juice = driver.find_element_by_css_selector("span.text-label")
        #first_juice.click()
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//div[2]/ul/li[3]/a/span/span/img").is_displayed():
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_xpath("//div[2]/ul/li[3]/a/span/span/span").click()
        driver.find_element_by_xpath("//img[@alt='Delete']").click()
        try:
            self.assertTrue(driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='English'])[1]/following::a[1]").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
