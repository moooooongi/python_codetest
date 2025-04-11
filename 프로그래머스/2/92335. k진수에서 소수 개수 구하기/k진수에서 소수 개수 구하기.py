import math
def is_prime(number):
    if number < 2 : return False
    for i in range(2, int(math.sqrt(number)+1)) :
        if number %i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    k_base = ''
    while n > 0:
        n,temp = divmod(n, k)
        k_base += str(temp)
    k_base = k_base[::-1].split("0")
    for i in k_base :
        if i == '' : continue
        if is_prime(int(i)) :
            answer += 1
    return answer