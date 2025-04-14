from itertools import combinations
def solution(n, q, ans):
    answer = 0
    #1~n까지모든 배열 돌아가기
    #q[i] 번째 원소와 몇개 맞는지 체크
    #ans[i]와 맞지 않을시 루프 다시 돌기
    #ans[i]와 맞으면 answer +1
    a = [i+1 for i in range(n)]
    b = combinations(a, 5)
    for var in b :
        for i,j in zip(q,ans):
            cnt = 0
            for k in var:
                if k in i:
                    cnt += 1
            if cnt != j:
                break
        else :
            answer += 1
    return answer