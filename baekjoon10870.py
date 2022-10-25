# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/10870
# 20221025

def fivo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fivo(n-1)+fivo(n-2)

n=int(input())
print(fivo(n))