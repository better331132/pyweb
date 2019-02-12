from flask import Flask, g, make_response, Response, request, session, render_template, Markup
from datetime import date, datetime, timedelta

app2 = Flask(__name__)

@app2.route("/aaa")
def aaa():
    return "connection"

