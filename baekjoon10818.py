# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/10818
# 20221025

n=int(input())
max=-1000000
min=1000000
input=input().split()
input=list(map(int,input))
for i in range(0,n):
    if input[i]>max:
        max=input[i]
    if input[i]<min:
        min=input[i]
print(min,max)