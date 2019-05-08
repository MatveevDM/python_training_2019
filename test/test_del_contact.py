from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="123", middlename="345", lastname="567", nickname="789", title="890", company="111", address="222"))
    app.contact.delete_first_contact()
