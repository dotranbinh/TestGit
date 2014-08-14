NAME, AGE, PAY= range(3)
bob=['Bob',30,30000]
print bob[AGE]
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
	print (person[0][0],person[0][1])
for person in people:
	for (name, value) in person:
		if name=='age': # find a specific field
			print value

#function to do this job for us
#define function

def field(record,lable):
	for(fname,value) in record:
		if (fname==lable):
			return value

print field(bob,'name')
for person in people:
	print field(person,'name')