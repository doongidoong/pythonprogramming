import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
cnt =0
def DFS(L):
    global cnt
    if L == n :
        if sum(check)==s and check:
            cnt+=1
        return
    check.append(g[L])
    DFS(L+1)
    check.pop(-1)
    DFS(L+1)
n,s = map(int, sys.stdin.readline().strip().split())
g = list(map(int, sys.stdin.readline().strip().split()))
g.sort()

check = []
DFS(0)

print(cnt)
    