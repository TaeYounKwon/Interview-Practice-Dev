from collections import deque

def check(s,begin):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer+=1
    if answer == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    dq = deque()
    dq.append([begin,[]])    
    
    while dq:
        curr,tmpList= dq.popleft()
        print('curr= ',curr,' list= ',tmpList)
        
        for word in words:
            if word not in tmpList and check(word, curr):
                if word == target:
                    return len(tmpList) + 1
                tmp = tmpList[0:]
                tmp.append(word)
                dq.append([word,tmp])
    
    return answer


words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin = 'hit'
target = 'cog'
solution(begin,target,words)