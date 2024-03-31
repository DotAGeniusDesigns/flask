from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations_map = {
    "add" : add,
    "sub" : sub,
    "mult" : mult,
    "div" : div
}

@app.route('/math/<operation>')
def do_math(operation):
    a = request.args.get('a', default = 0, type=int)
    b = request.args.get('b', default = 0, type=int)

    func = operations_map.get(operation)

    if func is None:
        return "Error: Not valid operation"
    
    try:
        result = func(a,b)
    except ZeroDivisionError:
        return "Error: Dividing by 0"
    
    return str(result)

@app.route('/add')
def addition():
    a = request.args.get('a', default = 0, type=int)
    b = request.args.get('b', default = 0, type=int)
    result = add(a,b)
    return str(result)

@app.route('/sub')
def subtraction():
    a = request.args.get('a', default = 0, type=int)
    b = request.args.get('b', default = 0, type=int)
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = request.args.get('a', default = 0, type=int)
    b = request.args.get('b', default = 0, type=int)
    result = mult(a,b)
    return str(result)

@app.route('/div')
def division():
    a = request.args.get('a', default = 0, type=int)
    b = request.args.get('b', default = 0, type=int)
    try:
        result = div(a,b)
    except ZeroDivisionError:
        return "Error: Dividing by 0"
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)