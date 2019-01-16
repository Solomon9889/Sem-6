#!/usr/bin/python

def eachlinek(line):
	words = line.split(' ')+line.split('(')
	
	word = 0
	for i in words:
		if((i == 'for') or (i == 'if') or (i == 'else') or (i == 'while') or (i == 'do') or  (i == 'break') or  (i == 'continue') or (i == 'int') or (i == 'double') or (i == 'float') or (i == 'return') or (i == 'char') or (i == 'case') or (i == 'char') or (i == 'sizeof') or (i == 'long')or (i == 'short') or (i == 'typedef') or (i == 'switch') or (i == 'unsigned') or (i == 'void') or (i == 'static') or (i == 'struct') or (i == 'goto')):
			word=word+1
	
	return word

def eachlineo(line):
	words = line.split(' ')
	
	word = 0
	for i in words:
		if((i == '+') or (i == '-') or (i == '*') or (i == '/') or (i == '%') or  ((i[1:3] == '++') or (i[0:2] == '++')) or ((i[1:3] == '--') or (i[0:2] == '--')) or (i == '<') or (i == '>') or (i == '<=') or (i == '>=') or (i == '=') ):
			word=word+1
	
	return word


def forkeyword(data):
	total = 0
	for i in data:
		count = eachlinek(i)
		total = total+ count
	print' 1) Total number of keywords:',total

def foroperator(data):
	total = 0
	for i in data:
		count = eachlineo(i)
		total = total+ count
	print' 2) Total number of operators:',total


f = open('geek.c','r')
data = f.readlines()
forkeyword(data)
foroperator(data)