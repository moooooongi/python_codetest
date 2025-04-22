def solution(numbers, hand):
    lh = [3,0]
    rh = [3,2]

    answer = ''
    pad = {
    1 : [0,0], 2 : [0,1] , 3 : [0,2],
    4 : [1,0], 5 : [1,1] , 6 : [1,2],
    7 : [2,0], 8 : [2,1] , 9 : [2,2],
    0 : [3,1]
    }
    for i in numbers :
        ans = pad[i]
        if ans[1] == 0 :
            lh = ans
            answer += "L"
        elif ans[1] == 2 :
            rh = ans
            answer += "R"
        else :
            lh_gap = abs(lh[0]-ans[0])+abs(lh[1]-ans[1])
            rh_gap = abs(rh[0]-ans[0])+abs(rh[1]-ans[1])
            if lh_gap < rh_gap :
                lh = ans
                answer += "L"
            elif rh_gap < lh_gap :
                rh = ans
                answer += "R"
            else :
                if hand == "right" :
                    rh = ans
                    answer += "R"
                else :
                    lh = ans
                    answer += "L"
    print(answer)
    
    return answer