def solution(n, lost, reserve):
    reserve,lost = sorted(set(reserve)-set(lost)), sorted(set(lost)-set(reserve))
    
    for i in lost[:]:
        if i-1 in reserve:
            reserve.remove(i-1)
            lost.remove(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
            lost.remove(i)
    answer = n - len(lost)
    return answer