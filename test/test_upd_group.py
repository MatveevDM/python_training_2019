# -*- coding: utf-8 -*-
from model.group import Group

def test_upd_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="new group"))
    app.session.logout()

def test_upd_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(header="new header"))
    app.session.logout()