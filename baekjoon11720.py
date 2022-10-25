# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/11720
# 20221025

sum=0
n=int(input())
numbers=input()

for i in range(0,n):
    sum+=int(numbers[i])

print(sum)