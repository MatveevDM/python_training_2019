# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("123")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("345")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("567")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("789")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("890")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("111")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("222")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
