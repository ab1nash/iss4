from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import itertools
from flask import Markup

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
quiz = SQLAlchemy(app)


class Questionclass(quiz.Model):
    id = quiz.Column(quiz.Integer, primary_key=True)
    Question = quiz.Column(quiz.String)
    Option1 = quiz.Column(quiz.String)
    Option2 = quiz.Column(quiz.String)
    Option3 = quiz.Column(quiz.String)
    Answer = quiz.Column(quiz.String)

    def __init__(self, Question, Option1, Option2, Option3, Answer):
        self.Question = Question
        self.Option1 = Option1
        self.Option2 = Option2
        self.Option3 = Option3
        self.Answer = Answer


@app.route('/')
def Quizzes():
    return render_template('Quizzes.html')


def addInquiz(Question, Option1, Option2, Option3, Answer):
    quiz.create_all()
    allUsers = Questionclass.query.all()
    new_item = Questionclass(Question, Option1, Option2, Option3, Answer)
    quiz.session.add(new_item)
    quiz.session.commit()

    def __repr__(self):
        return '<User %r>' % self.Question


@app.route("/view")
def userFetch():
    quiz.create_all()
    allUsers = Questionclass.query.all()
    diction = {"Questions": []}
    for x in allUsers:
        diction["Questions"].append({"Question": x.Question,
                                     "Option1": x.Option1,
                                     "Option2": x.Option2,
                                     "Option3": x.Option3,
                                     "Answer": x.Answer})
    return jsonify(diction)


addInquiz(
    "A hash function guarantees integrity of a message. It guarantees that message has not be", "Replaced","Over view","Changed",3)
addInquiz(
    "Digest created by a hash function is normally called a","Modification detection code (MDC)","Modify authentication connection","Message authentication control", 1)
addInquiz(
    "If a MAC tag is K-bits long, how much work is needed to find a collision to that specific value.","2^{k/2}",    "K^2",    "K!",3)
addInquiz(
"Best way to achieve both privacy and message integrity","Encrypt and Authenticate","Authenticate then Encrypt","Encrypt then Authenticate", 2)
addInquiz(
    " The out put length of SHA - I is _____________ bits","128","160","64",3)


if __name__ == '__main__':
    app.run(port='8080')
