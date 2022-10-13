from datetime import datetime
from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():

    return render_template('index.html', currentDate=datetime.now())


@app.get('/calculate')
def displayNumberPage():
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    number = request.form.get('number')
    if number is None or number == "":
        result = "No number provided"
    elif number.isdecimal():
        number = int(number)
        if number % 2 == 0:
            result = "Number " + str(number) + " is even"
        else:
            result = "Number " + str(number) + " is odd"
    else:
        result = "Provided input is not an integer!"

    return render_template('result.html', result=result)


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']

    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations
