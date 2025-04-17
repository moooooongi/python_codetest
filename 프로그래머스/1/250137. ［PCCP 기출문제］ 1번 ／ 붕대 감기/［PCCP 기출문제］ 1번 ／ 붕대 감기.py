def solution(bandage, health, attacks):
    t,x,y = bandage
    hp = health #hp
    time = 1 #지난시간
    a = 0 # 연속성공
    b = 0 # 공격횟수
    while b < len(attacks) :
        attacked = 0 #공격받지 않음
        if attacks[b][0] == time :
            hp -= attacks[b][1]
            attacked = 1 
            b += 1
            a = 0
        if hp <= 0 :
            return -1
        if attacked == 0 :
            a += 1
            if a==t :
                hp += x+y
                a = 0
            else :
                hp += x
        if hp > health:
            hp = health
        time += 1
    return hp