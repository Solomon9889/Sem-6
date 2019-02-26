#!/usr/bin/python


def forkeyword(data):
	
	
	checklist = []
	keyword = 0
	operators = 0
	special = 0
	identifiers = 0
	for a in data:
		words = a
		words = a.split(' ')
		
		if (words[0]=='printf'):
			
			words = words[0:1] 
			words.append(',')
			words.append('(')
			words.append(')')
			
		else:
			words = a.split(' ')
		
		
		
		for i in words:
			if((i == 'for') or (i == 'if') or (i == 'else') or (i == 'while') or (i == 'do') or  (i == 'break') or  (i == 'continue') or (i == 'int') or (i == 'double') or (i == 'float') or (i == 'return') or (i == 'char') or (i == 'case') or (i == 'char') or (i == 'sizeof') or (i == 'long')or (i == 'short') or (i == 'typedef') or (i == 'switch') or (i == 'unsigned') or (i == 'void') or (i == 'static') or (i == 'struct') or (i == 'goto')):
				keyword=keyword+1
				print(i+'      keyword')
			elif((i == '+') or (i == '-') or (i == '*') or (i == '/') or (i == '%') or  (i[1:3] == '++') or (i[0:2] == '++') or (i[1:3] == '--') or (i[0:2] == '--') or (i == '<') or (i == '>') or (i == '<=') or (i == '>=') or (i == '=') or (i == '&') or (i == '|') or (i == '^') or (i == '&&') or (i == '||') ):
				operators = operators+1
				print(i+'      operator')
			elif(True):
				
				i = i.replace('\n','')
				
				if((i == '[') or (i == ']') or (i == '{')or (i == '}')or (i == '(')or (i == ')')or (i == ';')or (i == ',')or (i == '*')):
					
					special = special +1
					print(i+'      specialsymbol')
				elif(i!=''):
					if( i in checklist):
						continue
					checklist.append(i)
					identifiers=identifiers+1
					print(i+'      identifier')
			
		
	print(' 1) Total number of keywords:',keyword)
	print(' 2) Total number of operators:',operators)
	print(' 3) Total number of special symbols:',special)
	print(' 4) Total number of identifiers:',identifiers)
			
		
	
f = open('geek.c','r')
data = f.readlines()
print('Token      Type')
forkeyword(data)
