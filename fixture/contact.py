

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # open add new
        wd.find_element_by_link_text("add new").click()
        self.enter_info_contact(contact, wd)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def enter_info_contact(self, contact, wd):
        # init contact creation
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("Last name").is_displayed()

    def update_first_contact(self, contact):
        wd = self.app.wd
        # submit updation
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.enter_info_contact(contact, wd)
        # save_info
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
