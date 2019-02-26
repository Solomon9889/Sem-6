
def update(lines):
    
    for i in lines:
	
        take(i)
        
def take(each_line):
     
    global LC
    
    each_line = each_line.replace("\n","")
    
    words = get_words(each_line)
    first = words[0]
    
    fp4 = open("output.txt","a+")
    fp4.write(str(LC)+' '+each_line+'\n')
    fp4.close()
    if (words[1]=='DC'or words[1]=='DS'):
            last=words[2]
            
            fp4 = open("st.txt","a+")
            fp4.write(first+' '+str(LC)+'\n')
            fp4.close()
            if(last[0]=='H'):
                    LC = (LC + 2)
            else:
                    LC = LC + 4
            
            
            
    elif(words[1]=='AR'):
            LC = LC + 2
    elif(words[1]=='START'):
            pass
    elif(words[1]=='USING'):
            pass
    elif(words[1]=='END'):
            pass
    else:
            flag = 0
            second = words[1]
            fp3 = open("mot.txt","r+")
            lines2 = fp3.readlines()
            for i in lines2:
                    if(i[0:2].strip(" ")==second):
                            flag = 1
                            break
            if(flag == 1):
                    LC = LC + 4
        
            fp3.close()

    

    

    
    

            

        
        
    
def get_words(each):
    words  = each.split(" ")
    
    return words
    
    
    
    
    

fp1 = open("input.txt","r+")



LC = 0
lines = fp1.readlines()
update(lines)
print(LC)

