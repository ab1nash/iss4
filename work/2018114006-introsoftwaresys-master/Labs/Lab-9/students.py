from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rollnumber = db.Column(db.Integer, unique=True)
    name=db.Column(db.String(80),unique=False)
    email = db.Column(db.String(120), unique=True)

    def _init_(self, rollnumber,name,email):
        self.rollnumber=rollnumber
        self.name=name
        self.email = email

    def _repr_(self):
        return '<User %r>' % self.username

@app.route("/students/create", methods=["POST","GET"])
def userAdd():
    rollnumber=request.form['rollnumber']
    name=request.form['name']
    email= request.form['email']
    db.create_all()
    new_person=User(rollnumber,name,email)
    db.session.add(new_person)
    db.session.commit()
    temp ={}
    temp['status']=(type(new_person)==User)
    return jsonify(temp)

@app.route("/students/",methods=["GET"])
def userFetch():
    db.create_all()
    allUsers=User.query.all()
    strf = ''
    for user in allUsers:
        strf += str(user.rollnumber) + " " +user.name + " " + user.email + "\n"
    return strf

@app.route("students/",methods=["POST","GET"])
def userUpdate():
    rno=request.form['rollnumber']
    nm=request.form['name']
    em=request.form['email']
    for user in allUsers:
        if(user.rollnumber==rno):
            user.name=nm
            user.email=em

            
@app.route("/students/delete",methods=["POST"])
def userDelete():
    rno=request.form['rollnumber']
    for user in allUsers:
        if(user.rollnumber==rno):
            me=user
    db.session.delete(me)
    db.session.commit(me)



if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
