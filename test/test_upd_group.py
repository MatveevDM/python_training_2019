# -*- coding: utf-8 -*-
from model.group import Group

def test_upd_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_contact(Group(name="777", header="888", footer="999"))
    app.session.logout()