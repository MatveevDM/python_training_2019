# -*- coding: utf-8 -*-
from model.contact import Contact

def test_upd_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(firstname="999", middlename="888", lastname="777", nickname="676", title="888", company="000", address="020"))
    app.session.logout()