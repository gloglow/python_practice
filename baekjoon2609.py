# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2609
# 20221026

#from math import gcd, lcm

def lcm(a,b):
    n=1
    while 1:
        if a*(n)%b==0:
            return a*n
        n+=1


def gcd(a,b):
    list=divisor_find(a)
    list.reverse()
    for i in list:
        if b%i==0:
            return i


def divisor_find(a):
    divisor_list=[]
    divisor_list.append(1)
    n=2
    while n<=a:
        if a%n==0:
            divisor_list.append(n)
        n+=1
    return divisor_list

a,b=map(int,input().split())

print(gcd(a,b))
print(lcm(a,b))
