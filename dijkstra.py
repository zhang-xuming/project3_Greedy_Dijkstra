import heap
import time

f=open('graph_4.txt','r')          #在此手动修改选择图
graph=[]
Z={}
next(f)
for line in f:
    line =line.replace("\n","")
    graph.append(list(map(int,line.split(' '))))        #读图
f.close()
for item in graph:                         #创建一个字典嵌套字典，里面存储每条边的信息
    if item[0] not in Z:
        Z[item[0]]={}
        Z[item[0]][item[1]] = item[2]
    else:
        if item[1] not in Z[item[0]] or Z[item[0]][item[1]] > item[2]:  #保证存入同向最小边
            Z[item[0]][item[1]]=item[2]
print(Z)

V=set()
X=set()
H=[]
for item in graph:                  #V集合存储所有点
    V.add(item[0])
    V.add(item[1])
A={}
p={}
for i in V:                         #初始化A值和p值
    A[i]=100000000
    p[i]='NULL'
s=int(input("please input start_node:"))
while s not in V:
    print("图中没这个点，请重新输入！")
    s = int(input("please input start_node:"))
d=int(input("please input destination_node:"))
while d not in V:
    print("图中没这个点，请重新输入！")
    d=int(input("please input destination_node:"))

t0=time.perf_counter()
X.add(s)
A[s]=0
left=0
if s in Z:                  #先访问s点
    for i in Z[s]:
        A[i]=Z[s][i]
        p[i]=s
for i in V:               #记录s点邻接边的信息
    if A[i]!=100000000:
        flag=[p[i],i,A[i]]
        heap.heap_insert(H,flag)
        left=left+1
while(V-X and left):         #循环终止条件，V中的所有点都找到了最短路或者堆里面没有元素了，其中left记录的是堆里面元素剩余个数
    m=heap.extract_min(H)    #取堆中最小值
    left=left-1
    while m[1] in X:
        m=heap.extract_min(H)
        left=left-1
    i=m[1]
    X.add(m[1])
    if i in Z:
        for t in Z[i]:
            if A[i]+Z[i][t]<A[t]:   #dijkstra的核心判断条件：是否满足贪心准则
                A[t]=A[i]+Z[i][t]   #记录满足贪心准则的邻接边信息
                p[t]=i
                flag=[p[t],t,A[t]]
                heap.heap_insert(H,flag)
                left=left+1


for i in V:                        #后面的都是输出格式
    print(i,end=':')
    print(A[i])
print()
if (p[d]=='NULL'):
    print('path:NULL')
else:
    print('path:',d,end='')
    while(d!=s):
        print("   <-   ",p[d],end='')
        d=p[d]
print()
print("running time:",time.perf_counter()-t0)
sum=0
for i in V:
    sum=sum+A[i]
print('sum:',sum)