def solution(n, words):
    already = []
    prev = ''
    cnt = 0
    p = 0
    isFailed = False
    for l in range(len(words)):
        p += 1
        if l%n == 0:
            cnt+=1
        if p>n:
            p-=n
        
        if l == 0:
            already.append(words[l])
            prev = words[l][-1]
            
        elif words[l][:1] == prev and words[l] not in already:
            already.append(words[l])
            prev = words[l][-1]
        else:
            isFailed = True
            break
    if isFailed == False:
        return [0,0]
    else:
        return [p,cnt]
    
def solution2(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]