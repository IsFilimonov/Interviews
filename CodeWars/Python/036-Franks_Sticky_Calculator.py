def sticky_calc(operation, val1, val2):
    v1 = int(round(val1))
    v2 = int(round(val2))
        
    stick = str(v1)+str(v2)
    
    if operation == '+':
        solution = int(stick) +v2
    elif operation == '-':
        solution = int(stick) - v2
    elif operation == '*':
        solution = int(stick) * v2
    elif operation == '/':
        solution = int(stick) / v2
        
    return round(solution)

## FYI
# eval() execute expression (eval("print('Привет')"))
# round(eval("{0}{1}{2}{1}".format(round(val1), round(val2), operation)))