# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2751
# 20221030
import sys

nlist=[]
for i in range(0, int(input())):
    nlist.append(int(sys.stdin.readline()))
nlist.sort()
for i in nlist:
    print(i)