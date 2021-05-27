def consecutive_ones(li):
    count = end = highest = 0

    for i in li:
        if i == 1:
            count += 1
            highest = count

        else:
            end = highest
            count = 0

    return "Number of consecutive one's are : {}".format(highest if highest > end else end)


lst1 = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
lst2 = [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]
print(consecutive_ones(lst1))
print(consecutive_ones(lst2))