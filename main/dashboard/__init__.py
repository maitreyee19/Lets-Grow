from flask import Flask , Blueprint

dashBoard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashBoard.route("/")
def show_dash_board():
    return "Daskboard will come here"
