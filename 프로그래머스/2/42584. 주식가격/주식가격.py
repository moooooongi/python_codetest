from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    
    while q :
        cnt = 0
        p = q.popleft()

        for i in q :
            if p <= i :
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

