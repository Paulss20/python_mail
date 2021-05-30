from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


# class BookManyHealthcareAppointments(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://mail.ru/"
#         self.verificationErrors = []
#         self.accept_next_alert = True


class LetterHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def test_book_many_healthcare_appointments(self):
        driver = self.driver
        driver.get("https://katalon-demo-cura.herokuapp.com/")



        # driver.find_element_by_name("q").click()
        # driver.find_element_by_name("q").clear()
        # driver.find_element_by_name("q").send_keys("mail")
        # driver.find_element_by_name("q").send_keys(Keys.ENTER)
        # driver.find_element_by_xpath("//div[@id='rso']/div/div/div/div/div/div/div/div/a/h3").click()
        # driver.find_element_by_name("login").click()
        # driver.find_element_by_name("login").click()
        # driver.find_element_by_name("login").clear()
        # driver.find_element_by_name("login").send_keys("pazoviy")
        # driver.find_element_by_name("domain").click()
        # Select(driver.find_element_by_name("domain")).select_by_visible_text("@list.ru")
        # driver.find_element_by_name("domain").click()
        # driver.find_element_by_xpath("//button[@type='button']").click()
        # driver.find_element_by_name("password").click()
        # driver.find_element_by_name("password").clear()
        # driver.find_element_by_name("password").send_keys("dalfin1972$")
        # driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        # driver.find_element_by_xpath(
        #     "//div[@id='app-canvas']/div/div/div/div/div[2]/span/div/div/div/div/div/div/div/div/a/span/span").click()
        # # ERROR: Caught exception [unknown command [editContent]]
        # driver.find_element_by_xpath("(//input[@value=''])[2]").click()
        # driver.find_element_by_xpath("//div[3]/div[3]/div").click()
        # driver.find_element_by_name("Subject").click()
        # driver.find_element_by_name("Subject").clear()
        # driver.find_element_by_name("Subject").send_keys("Themes")
        # driver.find_element_by_xpath("//div[5]/div/div/div[2]/div/div").click()
        # driver.find_element_by_xpath("//div[5]/div/div/div[2]/div/div[3]").click()
        # # ERROR: Caught exception [unknown command [editContent]]
        # driver.find_element_by_xpath("//div[2]/div/span/span/span").click()
        # driver.find_element_by_xpath("//div[9]/div/div/div[2]").click()




        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("pazoviy")
        driver.find_element_by_name("domain").click()
        driver.find_element_by_name("domain").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("dalfin1972$")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//div/div/div/div/div/a/span/span").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_xpath("(//input[@value=''])[2]").click()
        driver.find_element_by_xpath("//div[3]/div[3]/div").click()
        driver.find_element_by_name("Subject").click()
        driver.find_element_by_name("Subject").clear()
        driver.find_element_by_name("Subject").send_keys("Theme3")
        driver.find_element_by_xpath("//div[5]/div/div/div[2]/div/div").click()
        driver.find_element_by_xpath("//div[5]/div/div/div[2]/div/div[3]").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_xpath("//div[2]/div/span/span/span").click()
        driver.find_element_by_xpath("//div[9]/div/div/div[2]").click()
        driver.find_element_by_xpath("//span[3]").click()
        driver.find_element_by_xpath("//a[3]/div[2]").click()


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