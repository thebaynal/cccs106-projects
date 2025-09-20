# main.py
import flet as ft
from database import init_db
from app_logic import *


def main(page: ft.Page):
    # Page configuration
    page.title = "Contact Book"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window.maximized = True
    page.window_min_width = 400
    page.window_min_height = 600
    page.padding = 20
    page.spacing = 10
    

    # Initialize database
    db_conn = init_db()

    # Input fields
    name_input = ft.TextField(label="Name", width=350)
    phone_input = ft.TextField(label="Phone", width=350)
    email_input = ft.TextField(label="Email", width=350)
    inputs = (name_input, phone_input, email_input)

    # List view for contacts
    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=True)

    

    # Add button
    add_button = ft.ElevatedButton(
        text="Add Contact",
        on_click=lambda e: add_contact(page, inputs, contacts_list_view, db_conn),
    )

    # Page layout
    page.add(
        ft.Row(
            [
                # Left column (inputs + button)
                ft.Column(
                    [
                        ft.Text("Enter Contact Details:", size=20, weight=ft.FontWeight.BOLD),
                        name_input,
                        phone_input,
                        email_input,
                        add_button,
                    ],
                    spacing=10,
                    expand=1  # take available space
                ),

                ft.VerticalDivider(width=20, thickness=1, color=ft.Colors.GREY_300),
                
                # Right column (display contacts)
                ft.Column(
                    [
                        ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD),
                        contacts_list_view,
                    ],
                    spacing=10,
                    expand=2  # give more space to the contacts list
                )
            ],
            expand=True,
            spacing=30,  # space between columns
        )
    )

    # Display contacts on load
    display_contacts(page, contacts_list_view, db_conn)


if __name__ == "__main__":
    ft.app(target=main)
