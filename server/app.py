#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
        return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return parameter
    

@app.route("/count/<parameter>")
def count(parameter):
    print(parameter)
    num =""
    for item in range(0,10):
         num+=str(item) + "\n"
    return num

@app.route("/math/<int:num1><string:operation><int:num2>")
def math(num1, operation, num2):
    if operation ==  '+':
         return  str(num1 + num2)
    elif operation ==  '-':
         return  str(num1 - num2)
    elif operation ==  '*':
         return  str(num1 * num2)
    elif operation ==  'div':
         return  str(num1 / num2)
    elif operation ==  '%':
         return  str(num1 % num2)
    return 
        
    

    





if __name__ == '__main__':
    app.run(port=5555, debug=True)
