from flask import Flask, render_template, jsonify, request
from app import app
from vernam import *


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
    return render_template('Quizzes.html')


@app.route('/Further')
def Further():
    return render_template('Further.html')


@app.route('/Manual')
def Manual():
    return render_template('Manual.html')


@app.route('/Feedback')
def Feedback():
    return render_template('Feedback.html')



