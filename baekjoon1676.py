# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/1676
# 20221105

import math

n=int(input())
n=math.factorial(n)
tmp1=n//10
tmp2=n%10
cnt=0
while(tmp2==0 and tmp1!=0):
    n=n//10
    tmp1=n//10
    tmp2=n%10
    cnt+=1
print(cnt)