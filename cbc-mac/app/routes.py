from flask import Flask, render_template, jsonify, request,send_file
from app import app
from flask_sqlalchemy import SQLAlchemy
import random
import itertools
import sqlite3
#app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
quiz = SQLAlchemy(app)

class Questionclass(quiz.Model):
    id = quiz.Column(quiz.Integer, primary_key=True)
    Question = quiz.Column(quiz.String)
    Option1 = quiz.Column(quiz.String)
    Option2 = quiz.Column(quiz.String)
    Option3 = quiz.Column(quiz.String)
    Answer = quiz.Column(quiz.String)

    def __init__(self,Question, Option1,Option2, Option3,Answer):
        self.Question = Question
        self.Option1 = Option1
        self.Option2 = Option2
        self.Option3 = Option3
        self.Answer = Answer

@app.route('/')
@app.route('/Introduction')
def Introduction():
    return render_template('Introduction.html')


@app.route('/Theory')
def Theory():
    return render_template('Theory.html')


@app.route('/Procedure')
def Procedure():
    return render_template('Procedure.html')


@app.route('/Objective')
def Objective():
    return render_template('Objective.html')


@app.route('/Experiment')
def Experiment():
    return render_template('Experiment.html')


@app.route('/Quizzes')
def Quizzes():
    quiz.create_all()
    allUsers=Questionclass.query.all()
    global arr
    arr=random.sample(range(0, 5), 5)
    return render_template('Quizzes.html', Question1=allUsers[arr[0]],Question2=allUsers[arr[1]])



@app.route('/Further')
def Further():
    return render_template('Further.html')


@app.route('/Manual')
def Manual():
    return render_template('Manual.html')


@app.route('/Feedback')
def Feedback():
    return render_template('Feedback.html')



@app.route('/check', methods=['POST'])
def check():
    R1 = request.form['Q1']
    R2 = request.form['Q2']
    quiz.create_all()
    allUsers = Questionclass.query.all()
    Correct = "Correct Answers : "
    Wrong = "Wrong Answers : "
    Unattempted = "Unattempted  : "

    global arr
    if R1 == allUsers[arr[0]].Answer:
        Correct += "1 "
    elif R1 == '4':
        Unattempted += "1 "
    else:
        Wrong += "1 "
    if R2 == allUsers[arr[1]].Answer:
        Correct += "2 "
    elif R2 == '4':
        Unattempted += "2 "
    else:
        Wrong += "2 "
    Correct += "\n"
    Wrong += "\n"
    Unattempted += "\n"
    return jsonify({'output': Correct + Wrong + Unattempted})
