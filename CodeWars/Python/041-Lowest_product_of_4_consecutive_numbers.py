def lowest_product(input):
    if len(input) > 4:
        # range(len) -4 +1 because starts from 0 and upper range border cuts 1 point
        a = [list(map(int, list(input[i:i+4]))) for i in range(len(input)-4+1)]
        
        for i,v in enumerate(a):
            sum = 1
            for el in v:
                sum *= el
            a[i] = sum
          
        return min(a)
    else:
        return "Number is too small"

# FYA
# input = [*map(int, input)]
