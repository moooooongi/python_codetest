def solution(progresses, speeds):
    answer = []
    release = len(speeds) #배포할 작업 숫자
    cnt = 0 #배포하는데 걸린 일 수
    while release > 0 :
        cnt = 0 #한 번에 배포한 숫자
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        while progresses[len(speeds)-release] >= 100 :
            release -= 1
            cnt += 1
            if release <= 0 :
                break
        if cnt > 0 :
            answer.append(cnt)
    return answer