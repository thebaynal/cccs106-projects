# hello_flet.py
# CCCS 106 - Week 2 Lab Exercise
# First Flet GUI Application
# Student: Divino Al D. Ricafort

import flet as ft
from datetime import datetime


def main(page: ft.Page):
    """
    Main function for the Flet application.
    Everything you want to show or interact with will be defined here.
    """

    # -------------------------------
    # Page Configuration (Window setup)
    # -------------------------------
    page.title = "CCCS 106 - Hello Flet"   # Sets the window title
    page.window.width = 500                # Window width
    page.window.height = 400               # Window height
    page.padding = 20                      # Padding around the page
    page.theme_mode = ft.ThemeMode.LIGHT   # Theme (Light or Dark)

    # -------------------------------
    # Title Text (Header of the app)
    # -------------------------------
    title = ft.Text(
        "CCCS 106: Hello Flet Application",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLUE_700
    )

    # -------------------------------
    # Student Information Section
    # -------------------------------
    student_info = ft.Column([
        ft.Text("Student Information:", size=18, weight=ft.FontWeight.BOLD),
        ft.Text("Name: Divino Al D. Ricafort", size=14),
        ft.Text("Student ID: 231002032", size=14),
        ft.Text("Program: BSCS-3A", size=14),
        # Dynamically shows the current date
        ft.Text(f"Date: {datetime.now().strftime('%B %d, %Y')}", size=14),
    ])

    # -------------------------------
    # Interactive Section
    # -------------------------------

    # Input box where user types their name
    name_input = ft.TextField(
        label="Enter your name",
        width=300,
        border_color=ft.Colors.BLUE_300
    )

    # Placeholder text where greeting will appear
    greeting_text = ft.Text(
        "",
        size=16,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREEN_700
    )

    # -------------------------------
    # Button Functions
    # -------------------------------

    # Function to greet user with their entered name
    def say_hello(e):
        if name_input.value:  # If name is not empty
            greeting_text.value = f"Hello, {name_input.value}! Welcome to Flet GUI development!"
        else:
            greeting_text.value = "Please enter your name first!"
        page.update()  # Refresh the page with updated text

    # Function to clear the input and greeting text
    def clear_all(e):
        name_input.value = ""
        greeting_text.value = ""
        page.update()

    # Function to show information about the app in a dialog box
    def show_info(e):
        info_text = (
            "This is a Flet 0.28.3 application built for CCCS 106.\n"
            "Flet allows you to create beautiful GUI applications using Python!\n"
            f"Current time: {datetime.now().strftime('%I:%M:%S %p')}"
        )

        # Create and show dialog
        dialog = ft.AlertDialog(
            title=ft.Text("Application Information"),
            content=ft.Text(info_text),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_dialog(dialog))
            ]
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    # Helper function to close the info dialog
    def close_dialog(dialog):
        dialog.open = False
        page.update()

    # -------------------------------
    # Buttons with Styling
    # -------------------------------
    hello_button = ft.ElevatedButton(
        "Say Hello",
        on_click=say_hello,
        width=120,
        bgcolor=ft.Colors.BLUE_600,
        color=ft.Colors.WHITE
    )

    clear_button = ft.ElevatedButton(
        "Clear",
        on_click=clear_all,
        width=120,
        bgcolor=ft.Colors.GREY_600,
        color=ft.Colors.WHITE
    )

    info_button = ft.ElevatedButton(
        "App Info",
        on_click=show_info,
        width=120,
        bgcolor=ft.Colors.GREEN_600,
        color=ft.Colors.WHITE
    )

    # -------------------------------
    # Layout Arrangement
    # -------------------------------
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    title,
                    ft.Divider(height=20),  # Divider line for spacing
                    student_info,
                    ft.Divider(height=20),
                    ft.Text("Interactive Section:", size=16, weight=ft.FontWeight.BOLD),
                    name_input,
                    # Row of buttons (centered)
                    ft.Row(
                        [hello_button, clear_button, info_button],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Divider(height=10),
                    greeting_text,  # Shows output greeting
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=20
        )
    )


# -------------------------------
# Run the Application
# -------------------------------
if __name__ == "__main__":
    ft.app(target=main)
