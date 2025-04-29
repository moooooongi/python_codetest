def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reported = {}
    for a in report :
        i, j = a.split()
        if j in reported :
            if i in reported[j] :
                continue
            reported[j] = reported[j] + [i]
        else : reported[j] = [i]
    for b,c in reported.items():
        if len(c) >= k :
            for d in c :
                answer[id_list.index(d)]+=1
    return answer