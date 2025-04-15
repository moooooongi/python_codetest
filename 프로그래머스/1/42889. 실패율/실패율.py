def solution(N, stages):
    challenge = len(stages)
    sol = {}
    for i in range(1,N+1) :
        fail = stages.count(i)
        if challenge > 0 :
            sol[i] = fail/challenge
        else : 
            sol[i] = 0
        challenge -= fail
    temp = sorted(sol.items(), key = lambda x: (-x[1], x[0]))
    return [i[0] for i in temp]