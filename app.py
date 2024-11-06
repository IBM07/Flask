from flask import Flask,render_template,url_for,request,jsonify
import json
app=Flask(__name__)

@app.route('/')
def hi():
    return str(2)

@app.route('/cal',methods=(['GET']))
def calc():
    operation=request.json["operation"]
    n1=request.json["n1"]
    n2=request.json["n2"]
# if statement is demonstrated
    if operation=="add":
        return str(n1+n2)
    elif operation=="sub":
        return str(n1-n2)
    elif operation=="mul":
        return str(n1*n2)
    elif operation=="div":
        if n2!=0:
            return str(n1/n2)
        else:
            return "Division by Zero Not Possible"
    else:
        if n2!=0:
            return str(n1%n2)
        else:
            return "Division is done by zero so you won't get remainder"
    
    
if __name__=="__main__":
    app.run(debug=True)