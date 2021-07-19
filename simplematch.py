

def match(pattern,word):
    if pattern=='' and word=='':
        return True
    if pattern=='' and word!='':
        return False
    if word=='' and pattern!='':
        return False
    if word[0]!=pattern[0] and pattern[0]!='?':
        return False
    else:
        return match(pattern[1:],word[1:])

   