# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/1292
# 20221028

a,b=map(int,input().split())
sum=0 #합
start=1 #a 지점에서의 숫자
num=1 #더해질 숫자
next=1 #구간이 바뀌는 지점

while a>=next: #a 지점에서의 숫자와 다음 구간을 구한다.
    next+=num
    num+=1
num-=1

for i in range(a,b+1):
    if i==next:
        num+=1
        next+=num
    sum+=num
    
print(sum)