import sys
def dfs(L, sum):
    global max
    if L>n:
        return
    if L==n:
        if sum >max :
            max =sum
        return
    else:
        dfs(L+a[L][0], sum +a[L][1])
        dfs(L+1,sum)

max = 0


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","rt")


n = int(input())
a = list(tuple(map(int, input().split())) for _ in range(n))
dfs(0,0)
print(max)