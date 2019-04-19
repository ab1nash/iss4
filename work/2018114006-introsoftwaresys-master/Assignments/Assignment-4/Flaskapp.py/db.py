import sqlite3

db = sqlite3.connect('features.db')

cursor = db.cursor()

cursor.execute('''
	CREATE TABLE data(word TEXT, root TEXT,
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


# cursor.execute('''SELECT word, root, category, gender, num, person, cas, lan, cat, tense FROM data''')
# data1 = cursor.fetchall()
# for row in data1:
# 	print(row[0])