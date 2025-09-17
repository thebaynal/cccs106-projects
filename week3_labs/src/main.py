import flet as ft
import mysql.connector
from mysql.connector import Error
from db_connection import connect_db

def main(page: ft.Page):
    # Window setup
    page.title = "User Login"
    page.window.center()
    page.window.width = 400
    page.window.height = 350
    page.bgcolor = ft.Colors.AMBER_ACCENT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Title
    title = ft.Text(
        "User Login",
        size=20,
        weight=ft.FontWeight.BOLD,
        font_family="Arial",
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLACK,
    )

    # Username row
    username_field = ft.TextField(
        label="User name",
        hint_text="Enter your user name",
        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
        helper_text="This is your unique identifier",
        helper_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=250,
        autofocus=True,
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
        color=ft.Colors.BLACK,
        border_color=ft.Colors.BLACK,
    )

    username_row = ft.Row(
        controls=[
            ft.Container(
                content=ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLACK),
                alignment=ft.alignment.center,
                width=40
            ),
            username_field
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    # Password row
    password_field = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
        helper_text="This is your secret key",
        helper_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=250,
        password=True,
        can_reveal_password=True,
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT,
        color=ft.Colors.BLACK,
        border_color=ft.Colors.BLACK,
    )

    password_row = ft.Row(
        controls=[
            ft.Container(
                content=ft.Icon(ft.Icons.LOCK, color=ft.Colors.BLACK),
                alignment=ft.alignment.center,
                width=40
            ),
            password_field
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    # Dialog helpers
    def close_dialog(dlg):
        dlg.open = False
        if dlg in page.overlay:
            page.overlay.remove(dlg)
        page.update()

    success_dialog = ft.AlertDialog(
        content=ft.Column([
            ft.Icon(name=ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=40),
            ft.Text("Login Successful", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
            ft.Text("", text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(success_dialog))],
    )

    failure_dialog = ft.AlertDialog(
        content=ft.Column([
            ft.Icon(name=ft.Icons.ERROR, color=ft.Colors.RED, size=40),
            ft.Text("Login Failed", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
            ft.Text("Invalid username or password", text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(failure_dialog))],
    )

    invalid_input_dialog = ft.AlertDialog(
        content=ft.Column([
            ft.Icon(name=ft.Icons.INFO, color=ft.Colors.BLUE, size=40),
            ft.Text("Input Error", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
            ft.Text("Please enter username and password", text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(invalid_input_dialog))],
    )

    database_error_dialog = ft.AlertDialog(
        content=ft.Column([
            ft.Icon(name=ft.Icons.ERROR, color=ft.Colors.RED, size=40),
            ft.Text("Database Error", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
            ft.Text("An error occurred while connecting to the database", text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(database_error_dialog))],
    )

    # Login logic
    def login_click(e):
        if not username_field.value.strip() or not password_field.value.strip():
            if invalid_input_dialog not in page.overlay:
                page.overlay.append(invalid_input_dialog)
            invalid_input_dialog.open = True
            page.update()
            return

        conn = None
        try:
            conn = connect_db()
            if conn is None:
                if database_error_dialog not in page.overlay:
                    page.overlay.append(database_error_dialog)
                database_error_dialog.open = True
                page.update()
                return

            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username_field.value, password_field.value))
            result = cursor.fetchone()
            cursor.close()

            if result:
                success_dialog.content.controls[1].value = f"Welcome, {username_field.value}!"
                if success_dialog not in page.overlay:
                    page.overlay.append(success_dialog)
                success_dialog.open = True
            else:
                if failure_dialog not in page.overlay:
                    page.overlay.append(failure_dialog)
                failure_dialog.open = True

        except Error as err:
            print("Database error:", err)
            if database_error_dialog not in page.overlay:
                page.overlay.append(database_error_dialog)
            database_error_dialog.open = True

        finally:
            if conn and conn.is_connected():
                conn.close()

        page.update()

    # Login button
    login_btn = ft.ElevatedButton(
        text="Login",
        width=100,
        icon=ft.Icons.LOGIN,
        on_click=login_click,
    )

    # Final layout
    page.add(
        ft.Column(
            [
                title,
                ft.Column([username_row, password_row], spacing=20),
                ft.Container(
                    content=login_btn,
                    alignment=ft.alignment.top_right,
                    margin=ft.Margin(0, 20, 40, 0),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)