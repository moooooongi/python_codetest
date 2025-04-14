import math
def solution(fees, records):
    answer = []
    cars = {}
    for i in records :
        time, car, state = i.split()
        if car in cars.keys() : cars[car] = cars[car]+[time]
        else : cars[car] = [time]
    cars = {k:v for k,v in sorted(cars.items())}

    for i in cars.values():
        minutes = 0
        if len(i)%2 == 1 : i.append('23:59')
        print(i)
        for j in range(0,len(i),2):
            time_diff = int(i[j+1][:2])*60+int(i[j+1][-2:])- (int(i[j][:2])*60+int(i[j][-2:]))
            minutes += time_diff
            print(time_diff, minutes)
        if minutes <= fees[0] : answer.append(fees[1])
        else :
            price = fees[1] + math.ceil((minutes - fees[0])/fees[2])*fees[3]
            answer.append(price)
    return answer