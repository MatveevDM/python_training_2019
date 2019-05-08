# -*- coding: utf-8 -*-
from model.group import Group

def test_upd_group_name(app):
    app.group.update_first_group(Group(name="new group"))

def test_upd_group_header(app):
    app.group.update_first_group(Group(header="new header"))