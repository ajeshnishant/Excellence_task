def Sum(li):

    return sum(li)

def Sum_using_loop(li):
    sum = 0
    for i in li:
        sum +=i
    return sum


li = [i for i in range(10)]
print(Sum(li))
print(Sum_using_loop(li ))