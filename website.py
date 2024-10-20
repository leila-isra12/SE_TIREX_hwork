from flask import Flask,jsonify
from division import Division
from addition import Addition 
from multiplication import Multiplication
from substraction import Substraction

app = Flask (__name__) 
@app.route('/<operation>/<num1>/<num2>')
def calculator (operation , num1 , num2):
    if operation == "sum" : 
        op = Addition (float(num1) , float(num2))
        
    elif operation == "minus" : 
        op = Substraction (float (num1) , float (num2)) 
        
    elif operation == "divide" : 
        op = Division (float(num1) , float(num2))
       
    else : 
        op = Multiplication(float(num1) , float(num2))
       
    return  jsonify({
            "status" : 200 , 
            "result" : op.compute()   
    })
@app.route('/')
def landingpage () : 
    return "Welcome To Our Calculator "


if __name__ ==  '__main__' :
    app.run() 
