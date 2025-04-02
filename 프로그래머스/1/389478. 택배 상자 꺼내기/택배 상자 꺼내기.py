import math
def solution(n, w, num):
    floor_cnt = math.ceil(num/w)
    box_cnt = num
    answer = 0
    while n >= box_cnt :
        box_cnt += (floor_cnt*w - box_cnt)*2 + 1
        floor_cnt += 1
        answer += 1
    return answer