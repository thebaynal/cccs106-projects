# app_logic.py
import flet as ft
from database import *



def display_contacts(page, contacts_list_view, db_conn):
    """Fetches and displays all contacts in the ListView."""
    contacts_list_view.controls.clear()
    contacts = get_all_contacts_db(db_conn)

    for contact in contacts:
        contact_id, name, phone, email = contact

        contacts_list_view.controls.append(
            ft.ListTile(
                title=ft.Text(name),
                subtitle=ft.Text(f"Phone: {phone} | Email: {email}"),
                trailing=ft.PopupMenuButton(
                    icon=ft.Icons.MORE_VERT,
                    items=[
                        ft.PopupMenuItem(
                            text="Edit",
                            icon=ft.Icons.EDIT,
                            on_click=lambda _, c=contact: open_edit_dialog(
                                page, c, db_conn, contacts_list_view
                            ),
                        ),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Delete",
                            icon=ft.Icons.DELETE,
                            on_click=lambda _, cid=contact_id: delete_contact(
                                page, cid, db_conn, contacts_list_view
                            ),
                        ),
                    ],
                ),
            )
        )

    page.update()

def validate_inputs(name_input, phone_input, email_input, page):
    has_error = False

    # Reset all errors first
    for field in [name_input, phone_input, email_input]:
        field.error_text = None
        field.border_color = None

    # Check Name
    if not name_input.value.strip():
        name_input.error_text = "Name is required"
        name_input.border_color = ft.Colors.RED
        has_error = True

    # Check Phone
    if not phone_input.value.strip():
        phone_input.error_text = "Phone number is required"
        phone_input.border_color = ft.Colors.RED
        has_error = True

    # Check Email
    if not email_input.value.strip():
        email_input.error_text = "Email is required"
        email_input.border_color = ft.Colors.RED
        has_error = True

    page.update()
    return not has_error


def add_contact(page, inputs, contacts_list_view, db_conn):
    """Adds a new contact and refreshes the list."""
    name_input, phone_input, email_input = inputs

    if validate_inputs(name_input, phone_input, email_input, page):
        add_contact_db(
            db_conn,
            name_input.value,
            phone_input.value,
            email_input.value,
        )

        for field in inputs:
            field.value = ""

        display_contacts(page, contacts_list_view, db_conn)
        page.update()


def delete_contact(page, contact_id, db_conn, contacts_list_view):
    """Deletes a contact and refreshes the list."""
    delete_contact_db(db_conn, contact_id)
    display_contacts(page, contacts_list_view, db_conn)


def open_edit_dialog(page, contact, db_conn, contacts_list_view):
    """Opens a dialog to edit a contact's details."""
    contact_id, name, phone, email = contact

    edit_name = ft.TextField(label="Name", value=name)
    edit_phone = ft.TextField(label="Phone", value=phone)
    edit_email = ft.TextField(label="Email", value=email)

    def save_and_close(e):
        update_contact_db(
            db_conn,
            contact_id,
            edit_name.value,
            edit_phone.value,
            edit_email.value,
        )
        dialog.open = False
        page.update()
        display_contacts(page, contacts_list_view, db_conn)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Edit Contact"),
        content=ft.Column([edit_name, edit_phone, edit_email]),
        actions=[
            ft.TextButton(
                "Cancel",
                on_click=lambda e: setattr(dialog, "open", False) or page.update(),
            ),
            ft.TextButton("Save", on_click=save_and_close),
        ],
    )

    page.open(dialog)
