from flask import redirect, render_template, request, flash


def login_manager():
    if request.method == "POST":
        pass
    return "login.html"

def index_manager():
    if request.method == "POST":
        pass
    return "index.html"