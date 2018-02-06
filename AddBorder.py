def addBorder(picture):
    a = []
    for i in range(len(picture)):
        a+=[picture[i].replace(picture[i],'*'+picture[i]+'*')] 
    
    a.insert(0,'*'*len(a[0]))
    a.append('*'*len(a[0]))
    
    return a    
