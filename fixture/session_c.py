

class SessionContactHelper:

    def __init__(self, app_c):
        self.app_c = app_c

    def login(self, username, password):
        wd = self.app_c.wd
        self.app_c.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app_c.wd
        wd.find_element_by_link_text("Logout").click()