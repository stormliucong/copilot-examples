'''
create a flask app that can add, subtract, multiply, and divide
'''
from flask import Flask, request, jsonify
app = Flask(__name__)


def isdigits(x):
    '''
    check if x is a digit or not
    '''
    '''
    convert x to a string if possible
    '''
    x = str(x)
    if x.isdigit():
        return True
    else:
        return False

@app.route('/add', methods=['POST'])
def add():
    x = request.json['x']
    y = request.json['y']
    '''
    check if x and y are digits or not
    '''
    if isdigits(x) and isdigits(y):
        x = float(x)
        y = float(y)
        return jsonify(x + y)
    else:
        return jsonify('Invalid Input')
    

@app.route('/subtract', methods=['POST'])
def subtract():
    x = request.json['x']
    y = request.json['y']
    '''
    check if x and y are digits or not
    '''
    if isdigits(x) and isdigits(y):
        x = float(x)
        y = float(y)
        return jsonify(x - y)
    else:  
        return jsonify('Invalid Input')
    
@app.route('/multiply', methods=['POST'])
def multiply():
    x = request.json['x']
    y = request.json['y']
    '''
    check if x and y are digits or not
    '''
    if isdigits(x) and isdigits(y):
        x = float(x)
        y = float(y)
        return jsonify(x * y)
    else:
        return jsonify('Invalid Input')
    

@app.route('/divide', methods=['POST'])
def divide():
    x = request.json['x']
    y = request.json['y']
    '''
    check if x and y are digits or not
    '''
    if isdigits(x) and isdigits(y):
        x = float(x)
        '''convert y to float numbers'''
        y = float(y)
        if y == float(0):
            return jsonify('Cannot divide by zero')
        return jsonify(x / y)
    else:
        return jsonify('Invalid Input')

'''serve the app'''
if __name__ == '__main__':
    app.run(debug=True)

# $ python flask-example.py



