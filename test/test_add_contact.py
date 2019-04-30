# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.app_contact import App_contact


@pytest.fixture
def app_c(request):
    fixture = App_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app_c):
    app_c.session_c.login( username="admin", password="secret")
    app_c.contact.create(Contact(firstname="123", middlename="345", lastname="567", nickname="789", title="890", company="111", address="222"))
    app_c.session_c.logout()


def test_add_empty_contact(app_c):
    app_c.session_c.login(username="admin", password="secret")
    app_c.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address=""))
    app_c.session_c.logout()
