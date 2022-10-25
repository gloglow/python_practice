# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2460
# 20221025

n=0
max=0
for i in range(0,10):
    str=input().split()
    str=list(map(int,str))
    n=n-str[0]+str[1]
    if(n>max):
        max=n
print(max)