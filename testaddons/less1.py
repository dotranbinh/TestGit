
# wellcome lesson 1 of tutorial python language
#author Tran Binh Do

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
people=[bob,sue]
for person in people:
	print person[0].split()[1]
	person[2]*=1.20
for person in people:
	print person[2]
# collect all pay
pays=[person[2] for person in people]
print pays
pays= map((lambda x:x[0].split()[1]),people)
print list(pays)
sum= sum([person[2] for person in people])
print sum

tom=['Tom',30,30000,None]
people.append(tom)
print len(people)
print people[-1][0]
#exit