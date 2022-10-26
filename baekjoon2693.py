# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2693
# 20221026

n=int(input())
for i in range(0,n):
    nlist=input().split()
    nlist=list(map(int,nlist))
    nlist.sort()
    print(nlist[len(nlist)-3])
