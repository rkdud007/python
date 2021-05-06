import sys
import math

N, L, R = map(int,sys.stdin.readline().split()))
A = []
for r in range(N):
   A.append(list(map(int,sys.stdin.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def border(r,c):
    sum = 0
    now = A[r][c]
    if r <=-1 or r>= N or c<=-1 or c>=N :
        return False
    if now != -1:
        sum += now
        now = -1
        border(r-1,c,sum)
        border(r+1,c,sum)
        border(r,c-1,sum)
        border(r,c+1,sum)


    A[r][c] - A[r][c-1]  
 
for i in range(N):
    for k in range(N):
        result =  border(i,k)



    탐색한 나라는 -1로 바꾼다,연합조건 확인하고  연합 나라에 속한 인구를 다 더해서 연합 인구구하기 -> -1로 바꿨던 나라들에 다시 인구수 
    업데이트 해주기 ->  .... 연합 조건확인했는데 연합이 아무것도 없으면 종료 