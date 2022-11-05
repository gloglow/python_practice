# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/1789
# 20221104

s=int(input())

n=1

while(s>=0):
    s-=n
    n+=1

print(n-2)