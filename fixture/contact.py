

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, group_contact):
        wd = self.app.wd
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