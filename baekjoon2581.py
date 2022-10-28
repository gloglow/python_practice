# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2581
# 20221028

def prime_detector(a):
    if a==1:
        return False
    if a==2:
        return True
    for i in range(2, a):
        if a%i==0:
            return False
    return True

m=int(input())
n=int(input())
min=0
sum=0

for i in range(m, n+1):
    if prime_detector(i):
        sum+=i
        if min==0:
            min=i

if sum==0:
    print(-1)
else:
    print(sum)
    print(min)