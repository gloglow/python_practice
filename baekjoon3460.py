# BAEKJOON 3460 PROBLEM - https://www.acmicpc.net/problem/3460
# 20221024

""" 
def binary_one(i):
    tmp=0
    a=[]
    while i>0 :
        if i%2==1 :
            a.append(tmp)
        i=i//2
        tmp+=1
    return a

t=int(input())
tmp=t 
n=[]

while tmp>0:
    n.append(int(input()))
    tmp-=1

for i in n:
    for j in binary_one(i):
        print(j, end=' ')    
"""
"""
def bin_printing(n):
    for i in range(len(n)-1,-1,-1):
        if(n[i]=='1'):
            print(len(n)-1-i, end=' ')
    print()        

t=int(input())
for i in range(0,t):
    n=format(int(input()),'b')
    bin_printing(n)
"""