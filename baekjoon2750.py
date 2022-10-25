# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2750
# 20221025

n=int(input())
nlist=[]
for i in range(0,n):
    nlist.append(int(input()))
nlist.sort()
for i in range(0,n):
    print(nlist[i])