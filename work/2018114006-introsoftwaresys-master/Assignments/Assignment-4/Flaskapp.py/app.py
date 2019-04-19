from flask import Flask,render_template,request,jsonify, send_file
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import random
import itertools


db = sqlite3.connect('features.db', check_same_thread=False)
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS data(word TEXT, root TEXT,
                       category TEXT, gender TEXT, num TEXT, cas TEXT, person TEXT, lan TEXT, cat TEXT, tense TEXT)
	''')
db.commit()
	

cursor = db.cursor()

with open('features.txt', 'r') as f:
	for line in f:
		line1 = line.split(',')
		word1 = line1[0]
		root1 = line1[1]
		category1 = line1[2]
		gender1 = line1[3]
		num1 = line1[4]
		cas1 = line1[5]
		person1 = line1[6]
		lan1 = line1[7]
		cat1= line1[8]
		tense1 = line1[9]
		cursor.execute('''INSERT INTO data(word, root, category, gender, num, cas, person, lan, cat, tense)
						  VALUES(?,?,?,?,?,?,?,?,?,?)''', (word1, root1, category1, gender1, num1, cas1, person1, lan1, cat1, tense1))
		
    	
db.commit()

strings2 = list()

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

    def __init__(self,Question, Option1,Option2, Option3,Answer):
        self.Question = Question
        self.Option1 = Option1
        self.Option2 = Option2
        self.Option3 = Option3
        self.Answer = Answer

@app.route('/')
@app.route('/Introduction.html')
def index():
	return render_template('Introduction.html')

@app.route('/Theory.html')
def theory():
	return render_template('Theory.html')	

@app.route('/Objective.html')
def objective():
	return render_template('Objective.html')	

@app.route('/Experiment.html')
def experiment():
	return render_template('Experiment.html')	

@app.route('/Quizzes.html', methods=['POST', 'GET'])
def Quizzes():
    quiz.create_all()
    allUsers=Questionclass.query.all()
    global arr
    arr=random.sample(range(0, 9), 5)
    return render_template('Quizzes.html', Question1=allUsers[arr[0]],Question2=allUsers[arr[1]],Question3=allUsers[arr[2]],Question4=allUsers[arr[3]],Question5=allUsers[arr[4]])

@app.route('/Procedure.html')
def procedure():
	return render_template('Procedure.html')		

@app.route('/Feedback.html')
def feedback():
	return render_template('Feedback.html')	

@app.route('/Further Readings.html')
def further():
	return render_template('Further Readings.html')	

@app.route('/file')
def read():
	return send_file('./static/features2.txt', attachment_filename='features2.txt')

@app.route('/check',methods= ['POST'])
def check():
    R1=request.form['Q1']
    R2=request.form['Q2']
    R3=request.form['Q3']
    R4=request.form['Q4']
    R5=request.form['Q5']
    quiz.create_all()
    allUsers=Questionclass.query.all()
    Correct="Correct Answers : "
    Wrong="Wrong Answers : "
    Unattempted="Unattempted  : "
    
    global arr
    if R1==allUsers[arr[0]].Answer:
        Correct+="1 "
    elif R1=='4':
        Unattempted+="1 "
    else:
        Wrong+="1 "
    if R2==allUsers[arr[1]].Answer:
        Correct+="2 "
    elif R2=='4':
        Unattempted+="2 "
    else:
        Wrong+="2 "
    if R3==allUsers[arr[2]].Answer:
        Correct+="3 "
    elif R3=='4':
        Unattempted+="3 "
    else:
        Wrong+="3 "
    if R4==allUsers[arr[3]].Answer:
        Correct+="4 "
    elif R4=='4':
        Unattempted+="4 "
    else:
        Wrong+="4 "
    if R5==allUsers[arr[4]].Answer:
        Correct+="5 "
    elif R5=='4':
        Unattempted+="5 "
    else:
        Wrong+="5 "
    Correct+="\n"
    Wrong+="\n"
    Unattempted+="\n"
    return jsonify({'output':Correct+Wrong+Unattempted})	

@app.route('/process',methods=['POST'])	
def process():
	cursor = db.cursor()
	word1 = request.form['word']
	root1 = request.form['root']
	category1 = request.form['category']
	gender1 = request.form['gender']
	num1 = request.form['number']
	cas1 = request.form['case']
	person1 = request.form['person']
	tense1 = request.form['tense']

	cursor.execute('''SELECT word, root, category, gender, num, cas, person, lan, cat, tense FROM data WHERE root=? and category=? and gender=? and num=? and cas=? and person=? and tense=?''', (root1, category1, gender1, num1, cas1, person1, tense1,))
	strings2.clear()	
	all_rows = cursor.fetchall()
	for row in all_rows:
		strings2.append(row[0])
		# print(row[0])
	

	flag = 0
	cnt = 0
	for st in strings2:
		cnt = cnt + 1
		if st == word1:
			flag = 1

	str = "NONE" 
	if ( (cnt == 0) and (word1 == str) ):
		return jsonify({'answer' : "Right Answer!!"})

	else:
		if flag == 1:
			return jsonify({'answer' : "Right Answer!!"})
		else:
			if ( cnt != 0 ):
				return jsonify({'answer' : "Wrong Answer!!",
								'right_answer' : "Answer:" + " " +  strings2[0]})
			else:
				return jsonify({'answer' : "Wrong Answer!!",
								'right_answer' : "Answer: Word with such features does not exist"})
	
		

if __name__  ==  '__main__':
	app.run(debug=True)

