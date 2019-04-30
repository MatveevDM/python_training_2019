from selenium import webdriver
from fixture.session_c import SessionContactHelper


class App_contact:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_c = SessionContactHelper(self)


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()
        self.session_contact = SessionContactHelper(self)

    def create_contact(self, group_contact):
        wd = self.wd
        # open add new
        wd.find_element_by_link_text("add new").click()
        # init contact creation
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group_contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group_contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group_contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group_contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group_contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group_contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group_contact.address)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
