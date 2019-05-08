# -*- coding: utf-8 -*-
from model.contact import Contact

def test_upd_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="123", middlename="345", lastname="567", nickname="789", title="890", company="111", address="222"))
    app.contact.update_first_contact(Contact(firstname="999", middlename="888", lastname="777", nickname="676", title="888", company="000", address="020"))