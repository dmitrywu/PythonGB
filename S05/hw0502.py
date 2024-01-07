def sum(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return sum(a+1, b-1)
    

# def rec_sum(a, b):
#    return a if b == 0 else rec_sum(a+1, b-1) if b > 0 else rec_sum(a-1, b+1)

a = 2
b = 3
print(sum(a, b))