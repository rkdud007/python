import sys
N= int(sys.stdin.readline())

case = []
for i in range(N):
    case.append(list(sys.stdin.readline().rstrip()))
print(case)
if case[0][1] == '1':
    print(123124)

def dfs(x,y,ctn):
    if x <=-1 or x>= N or y<=-1 or y>=N :
        return ctn
    if case[x][y] == '1':
        case[x][y] ='0'
        ctn = dfs(x-1,y,ctn+1)
        ctn = dfs(x,y-1,ctn+1)
        ctn = dfs(x,y+1,ctn+1)
        ctn = dfs(x+1,y,ctn+1)
        return ctn
    return ctn

total_num = 0
result = 0
house_num = []
for i in range(N):
    for k in range(N):
        ctn =0
        result = dfs(i,k,ctn)
        print(result)
        if result != 0:
            total_num +=1
            house_num.append(result)

print(house_num)
house_num.sort()
print(total_num)
for i in house_num:
    print(i)