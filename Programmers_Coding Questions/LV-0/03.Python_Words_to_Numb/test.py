def solution(numbers):
    answer = ''
    numb_list =  {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }
    tmp = ''
    for i in range(len(numbers)):
        tmp += numbers[i]

        if answer =='' and tmp == 'zero':
            return False
        
        if tmp in numb_list.keys():
            answer+=str(numb_list[tmp])
            tmp = ''
    answer = int(answer)
    return answer

test = "onetwothreefourfivesixseveneightnine"
if solution(test) == 123456789:
    print('Pass')
else:
    print('Failed')