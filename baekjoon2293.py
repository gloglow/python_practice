# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2293
# 20221126

tmp=input().split()
n=int(tmp[0])
k=int(tmp[1])
coins=[]
sum_list=[0 for i in range(100000)]
sum_list[0]=1

for _ in range(n):
    coins.append(int(input()))


for i in range(0, n):
    for j in range(coins[i], k+1):
        sum_list[j]+=sum_list[j-coins[i]]

print(sum_list[k])