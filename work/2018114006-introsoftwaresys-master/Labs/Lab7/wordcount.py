import sys
f = open(sys.argv[1] , "rt")
g = open(sys.argv[2] , "w")
g.write("")
g.close()

text=f.read().lower().replace("," , "").replace("." , "").replace(":" , "").replace(";" , "").replace("!" , "").replace("?" , "").replace("\"\"","").replace("(","").replace(")","")
listtext=text.split(" ")
count = {}
for i in listtext:
	if i in count:
		continue
	else:
		count[i]=listtext.count(i)
for i in count:
	g = open(sys.argv[2] , "a")
	g.write(i+" : "+str(count[i]) + "\n")
	g.close()