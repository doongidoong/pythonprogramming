import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n =int(input())
a=[ list(map(int,input().split())) for _ in range(n)] 

for i in range(1,n):
    a[i][0] += min(a[i-1][1],a[i-1][2]) 
    a[i][1] += min(a[i-1][0],a[i-1][2]) 
    a[i][2] += min(a[i-1][0],a[i-1][1])

print(min(a[n-1])) 
    