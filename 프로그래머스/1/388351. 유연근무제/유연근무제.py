def cal_time(hope,real,startday):
    hope_h, hope_m = divmod(hope,100)
    real_h, real_m = divmod(real,100)
    if hope >= real or startday >= 6: 
        return 0
    elif real_m - hope_m < 0 :
        real -= 40
    return real-hope
def solution(schedules, timelogs, startday):
    answer= 0
    for i,j in enumerate(timelogs) :
        std = startday
        gj = 0
        for k in j :
            if cal_time(schedules[i],k,std) <= 10 : gj += 1
            if std == 7 : std = 1
            else : std += 1
        if gj == 7 : answer += 1
    return answer
