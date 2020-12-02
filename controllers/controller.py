from app import app
from modules.calculator import add
from modules.calculator import subtract
from modules.calculator import multiply
from modules.calculator import divide


@app.route("/")
def index():
    return "Calculator Homepage"

@app.route("/add/<num_1>/<num_2>")
def addanswer(num_1, num_2):
    return f"{num_1} + {num_2} = {add(num_1,num_2)}"

@app.route("/subtract/<num_1>/<num_2>")
def subtractanswer(num_1, num_2):
    return f"{num_1} - {num_2} = {subtract(num_1,num_2)}"

@app.route("/divide/<num_1>/<num_2>")
def divideanswer(num_1, num_2):
    return f"{num_1} / {num_2} = {divide(num_1,num_2)}"

@app.route("/multiply/<num_1>/<num_2>")
def multiplyanswer(num_1, num_2):
    return f"{num_1} x {num_2} = {multiply(num_1,num_2)}"