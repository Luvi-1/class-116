#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():
    name = "Lavi"
    age = '15'
 
    return render_template('index.html', name = name , age = age)
@app.route("/Father")

#‘/’ URL is bound with first_flask function.
def father():
    name = "happy"
    age = '47'
 
    return render_template('Father.html', name = name , age = age)


#run the application on local server
app.run()
