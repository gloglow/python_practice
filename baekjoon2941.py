# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/2941
# 20221101

word=input()
sum=len(word)
check=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in check:
    sum-=word.count(i)
print(sum)

"""
word=input()
sum=len(word)
for i in range(0,len(word)):
    if word[i]=='=':
        if (word[i-1]=='c') or (word[i-1]=='s'):
            sum-=1
        elif word[i-1]=='z':
            sum-=1
            if word[i-2]=='d':
                sum-=1
    if word[i]=='-':
        if (word[i-1]=='c') or (word[i-1]=='d'):
            sum-=1
    if word[i]=='j':
        if i-1>=0 and ((word[i-1]=='l') or (word[i-1]=='n')):
            sum-=1
print(sum)
"""