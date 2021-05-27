user = {"1": "name1", "2": "name2", "3": "name3"}
dict1 = {"1": 50, "2": 80, "3": 70}


def maximum(dic):
    key = max(dic, key=dic.get)
    return dict({key: dic[key]})


def maximum_2(dic):
    v = list(dic.values())

    # taking list of car keys in v
    k = list(dic.keys())

    key = k[v.index(max(v))]
    return dict({key: dic[key]})


print(maximum(dict1))
print(maximum_2(dict1))
