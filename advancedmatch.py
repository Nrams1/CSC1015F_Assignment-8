

def match(pattern,word):
    if  word!="" and pattern=="*":
        return True
    if pattern=='' and word=='':
        return True
    if pattern=='' and word!='':
        return False
    if word[0]!=pattern[0] and pattern!='':
        return True
    if word[0]!=pattern[0] and pattern[0]=='?':
        return True
    
    else:
        if pattern[0]!="*":
            if pattern[0]==word[0]:
                return match(pattern[1:],word[1:])
        else:
            new_pattern=pattern[1:]
            print(new_pattern,word)
            if word.find(new_pattern)>=0:
                return True
               
        
            
            
