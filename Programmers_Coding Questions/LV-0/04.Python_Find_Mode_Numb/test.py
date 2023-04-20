def solution(array):
    while len(array) !=0:
        for i, a in enumerate(set(array)):
            print(i, a)
            array.remove(a)
        print(i, a)
        if i == 0: return a
    return -1

def solution2(array):
    answer = 0
    tmp = dict()
    for i in array:
        if i not in tmp.keys():
            tmp[i]=1
        else:
            tmp[i]+=1

    max_val = max(tmp.values())
    tmpValue = list(tmp.values())


    if tmpValue.count(max_val)>1:
        return -1

    for keys, values in tmp.items():
        if values == max_val:
            return keys
