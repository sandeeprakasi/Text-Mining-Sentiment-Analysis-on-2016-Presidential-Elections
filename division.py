import re

def test():
	input=open('data.txt','r')
	output=open('hillary.txt','w')
	check=open('hashhillary.txt','r')
	input_l=list()
	check_l=list()
	for word in check :
		word=word.rstrip('\n')
		i=check_l.append(word)	
	for line in input:
		line=line.rstrip('\n')
		l=input_l.append(line)
	for w in check_l:
		for li in input_l:
			if w in li:
				#print li
				output.write(li + '\n')
	output.close()
				

a=test()		
