# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
import time




class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.kazidomi.com/en-FR")
        driver.maximize_window()
        driver.find_element_by_xpath("//img[@alt='My Account']").click()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("yagekod805@porjoton.com")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("truePath12345")
        driver.find_element_by_id("inputEmail").click()
        driver.find_element_by_id("inputPassword").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//img[@alt='My Account']").click()
        driver.find_element_by_link_text("My wish list").click()
        driver.find_element_by_name("wishlist").click()
        driver.find_element_by_name("wishlist").clear()
        driver.find_element_by_name("wishlist").send_keys("fresh_list2")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #driver.find_element_by_link_text("MyNew_wishlist1").click()
        #driver.find_element_by_xpath(
            #"(.//*[normalize-space(text()) and normalize-space(.)='Select'])[1]/following::a[1]").click()
        driver.find_element_by_css_selector("div.account-nav-select > ul > li:nth-child(12) > a").click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.homepage-intro-header-left"))).get_attribute("Products that do good")
            #"(.//*[normalize-space(text()) and normalize-space(.)='Previously purchased products'])[2]/following::a[1]").click()

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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

