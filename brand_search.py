# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class ShopSearchingByBrand(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_shop_searching_by_brand(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.kazidomi.com/en-FR/shop")
        driver.find_element_by_id("search_query_top").click()
        driver.find_element_by_id("search_query_top").clear()
        driver.find_element_by_id("search_query_top").send_keys("juice")
        time.sleep(3)
        driver.find_element_by_xpath("//span[@id='hitsSearchBar']/ul/li[12]/a/span").click()
        driver.find_element_by_link_text("Add 1 to cart").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/ul/li[3]/a/span/span/img").is_displayed()
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
