# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/4673
# 20221030

def sum_of(i):
    sum=0
    sum+=i%10
    while i>=10:
        i=i//10
        sum+=i%10
    return sum

nlist=[]
for i in range(1,10001):
    nlist.append(i)
for i in range(1,10001):
    num=i+sum_of(i)
    if num in nlist:
        nlist.remove(num)
for i in nlist:
    print(i)
