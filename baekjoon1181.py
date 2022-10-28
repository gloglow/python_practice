# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/1181
# 20221028

n=int(input())
sorting_flag=0
word_set=set()
for i in range(0,n):
    word_set.add(input())

word_list=list(word_set)
word_list.sort(key=len)

pre_len=len(word_list[0])
pre_index=0

for i in range(1,len(word_list)):
    current_len=len(word_list[i])
    if pre_len<current_len:
        if sorting_flag==1:
            word_list[pre_index:i]=sorted(word_list[pre_index:i])
            sorting_flag=0
        pre_len=current_len
        pre_index=i
    else:
        sorting_flag=1

if pre_len==len(word_list[len(word_list)-1]):
    word_list[pre_index:len(word_list)]=sorted(word_list[pre_index:len(word_list)])

for i in range(0, len(word_list)):
    print(word_list[i])