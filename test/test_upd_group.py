# -*- coding: utf-8 -*-
from model.group import Group

def test_upd_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(Group(name="new group"))

def test_upd_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test header"))
    app.group.update_first_group(Group(header="new header"))