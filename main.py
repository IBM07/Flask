from flask import Flask,request,render_template,jsonify
import json

app=Flask(__name__)
#obj=Flask(__name__)
@app.route("/")
def hi():
    return str(5+9)

@app.route("/b")
def he():
    return str(10+9)

@app.route("/calc",methods=(['GET']))
def calc(): 
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    if operation=="a":
        return str(num1+num2)
    elif operation=="m":
        return str(num1*num2)
    elif operation=="s":
        return str(num1-num2)
    else:
        return str(num1/num2)
    
if __name__=="__main__":
    app.run()
    #obj.run()