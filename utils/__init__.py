from os import getenv
from flask import redirect, url_for


def handle_login(form):
    if authenticate_admin(form.email, form.password):
        return redirect(url_for("success"))

    return redirect(url_for("denied"))


def authenticate_admin(email, password):
    is_valid_email = email.data == getenv("ADMIN_EMAIL")
    is_valid_password = password.data == getenv("ADMIN_PASSWORD")

    return is_valid_email and is_valid_password
