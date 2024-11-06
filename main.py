from flask import Flask,request,render_template

app=Flask(__name__)
#obj=Flask(__name__)
@app.route("/")
def hi():
    return str(5+9)

@app.route("/b")
def he():
    return str(10+9)

@app.route("/calc")
def calc():
    operation="r"
    num1=int(input("Enter 1st Number : "))
    num2=int(input("Enter 2nd Number : "))
    if operation=="a":
        return str(num1+num2)
    elif operation=="m":
        return str(num1*num2)
    elif operation=="s":
        return str(num1-num2)
    else:
        return str(num1/num2)
    
if __name__=="__main__":
    app.run(debug=True)
    #obj.run()