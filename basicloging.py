# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


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
        driver.maximize_window()
        driver.get("https://www.kazidomi.com/en-FR")
        for i in range(60):
            try:
                if driver.find_element_by_xpath("//img[@alt='My Account']").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//img[@alt='My Account']").click()
        driver.find_element_by_id("inputEmail").clear()
        driver.find_element_by_id("inputEmail").send_keys("yagekod805@porjoton.com")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("truePath12345")
        driver.find_element_by_id("inputEmail").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//img[@alt='My Account']").click()
        driver.find_element_by_link_text("My Account").click()
        driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Previously purchased products'])[2]/following::a[1]").click()

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