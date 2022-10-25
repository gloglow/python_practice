# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2309
# 20221025

nlist=[]
finish=0

for i in range(0,9):
    nlist.append(int(input()))
nlist.sort()
for i in range(0,9):
    for j in range(i+1,9):
        if sum(nlist)-nlist[i]-nlist[j]==100:

            finish=1
            break
    if finish==1:
        break        
            
for k in range(0,9):
    if k!=i and k!=j:
        print(nlist[k])