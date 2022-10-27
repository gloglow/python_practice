# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/1978
# 20221027

n=int(input())
nlist=input().split()
nlist=list(map(int,nlist))
result=len(nlist)
for i in range(0,n):
    if nlist[i]==1:
        result-=1
        continue
    for j in range(2,nlist[i]):
        if(nlist[i]%j==0):
            result-=1
            break
print(result)                