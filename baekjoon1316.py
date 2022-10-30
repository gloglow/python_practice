# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/1316
# 20221029

result=0
for i in range(int(input())):
    str=input()
    if list(str)==sorted(str,key=str.find):
        result+=1
print(result)

"""
result=0
flag=1
for i in range(0,n):
    str=input()
    for j in range(0,len(str)):
        for k in range(j+1,len(str)):
            if str[j]==str[k]:
                j=k
            else:
                for l in range(k+1, len(str)):
                    if str[l]==str[j]:
                        flag=0
                        break
            if flag==0:
                break
        if flag==0:
            break
    if flag==1:
        result+=1
    else:
        flag=1

print(result)
"""