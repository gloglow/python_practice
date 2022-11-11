# BAEKJOON  PROBLEM - https://www.acmicpc.net/problem/3085
# 20221111

import re

def count_candy_color(n, board, color):
    max=0
    res=color+r'+'
    for i in range(0, n):
        board_row=''.join(c for c in board[i])
        start=-1
        while 1:
            if start==-1: 
                start=0
            else:
                start+=len(rlist.group())
                if start>=n:
                    break
            rlist=re.search(res, board_row[start:])
            if rlist==None:
                break
            start+=rlist.start()
            if i>0:
                if start>0:
                    if board[i-1][start-1]==color:
                        tmp=len(rlist.group())+1
                        j=start-2
                        while j>=0:
                            if board[i][j]==color:
                                j-=1
                                tmp+=1
                            else:
                                break
                        if tmp>max:
                            max=tmp
                    if start-2>=0 and board[i][start-2]==color:
                        tmp=len(rlist.group())+1
                        if tmp>max:
                            max=tmp
                    if start+len(rlist.group())+1<n and board[i][start+len(rlist.group())+1]==color:
                        tmp=len(rlist.group())+1
                        if tmp>max:
                            max=tmp
                if start+rlist.end()<n:
                    if board[i-1][start+len(rlist.group())]==color:
                        tmp=len(rlist.group())+1
                        j=start+len(rlist.group())+1
                        while j<n:
                            if board[i][j]==color:
                                j+=1
                                tmp+=1
                            else:
                                break
                        if tmp>max:
                            max=tmp
                    if start-2>=0 and board[i][start-2]==color:
                        tmp=len(rlist.group())+1
                        if tmp>max:
                            max=tmp
                    if start+len(rlist.group())+1<n and board[i][start+len(rlist.group())+1]==color:
                        tmp=len(rlist.group())+1
                        if tmp>max:
                            max=tmp
                for k in range(start, start+len(rlist.group())):
                    if board[i-1][k]==color:
                        tmp=len(rlist.group())
                        if tmp>max:
                            max=tmp
                        break
            if i<n-1:
                if start>0:
                    if board[i+1][start-1]==color:
                        tmp=len(rlist.group())+1
                        j=start-2
                        while j>=0:
                            if board[i][j]==color:
                                j-=1
                                tmp+=1
                            else:
                                break
                        if tmp>max:
                            max=tmp
                if start+rlist.end()<n:
                    if board[i+1][start+len(rlist.group())]==color:
                        tmp=len(rlist.group())+1
                        j=start+len(rlist.group())+1
                        while j<n:
                            if board[i][j]==color:
                                j+=1
                                tmp+=1
                            else:
                                break
                        if tmp>max:
                            max=tmp
                for k in range(start, start+len(rlist.group())):
                    if board[i+1][k]==color:
                        tmp=len(rlist.group())
                        if tmp>max:
                            max=tmp
                        break
            if max<len(rlist.group())-1 and n==2:
                tmp=len(rlist.group())-1
                if tmp>max:
                            max=tmp
                continue
            else:
                tmp=len(rlist.group())
                if tmp>max:
                            max=tmp
                continue
    return max   

def count_candy_entire(n, board):
    max=count_candy_color(n, board, 'C')
    tmp=count_candy_color(n, board, 'P')
    if max<tmp:
        max=tmp
    tmp=count_candy_color(n, board, 'Z')
    if max<tmp:
        max=tmp
    tmp=count_candy_color(n, board, 'Y')
    if max<tmp:
        max=tmp
    return max
        
n=int(input())
board=[]
for i in range(0, n):
    tmp=input()
    board.append([])
    for j in range(0, n):
        board[i].append(tmp[j])

max=count_candy_entire(n, board)
max2=count_candy_entire(n, list(map(list, zip(*board))))

if max<max2: 
    max=max2
print(max)