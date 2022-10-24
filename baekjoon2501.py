# BAEKJOON 2501 PROBLEM - https://www.acmicpc.net/problem/2501
# 20221024

n, k = map(int, input().split())

nlist=[]
tmp=1
k=k-1

while tmp<n:
    if n%tmp==0:
        nlist.append(tmp)
    tmp=tmp+1
if k<=len(nlist):
    print(nlist[k]) 
