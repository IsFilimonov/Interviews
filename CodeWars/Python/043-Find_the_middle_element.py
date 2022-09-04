def gimme(a):      
    min_indx = a.index(min(a))
    max_indx = a.index(max(a))
    
    return int('012'.replace(str(min_indx),'').replace(str(max_indx),''))

# FYA Best practice
# def gimme(a):
#     return a.index(sorted(a)[1])