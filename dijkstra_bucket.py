import bucket
import time

f=open('graph_4.txt','r')
graph=[]
Z={}
next(f)
for line in f:
    line =line.replace("\n","")
    graph.append(list(map(int,line.split(' '))))     #从文本文件中读图
f.close()
num=0
for item in graph:                      #建立一个字典嵌套字典，存储所有有向边的信息
    if item[0] not in Z:
        Z[item[0]]={}
        Z[item[0]][item[1]] = item[2]
    else:
        if item[1] not in Z[item[0]] or Z[item[0]][item[1]]>item[2]:
            Z[item[0]][item[1]]=item[2]
    if item[2]>num:                   #用num记录边的最大权重
        num=item[2]
print(Z)
num=num+1                        #num=num+1，方便后面调用

V=set()
X=set()
left=0
B=bucket.built_bucket(num)          #建立num+1个桶
location=[0]
for item in graph:                 #用V记录图中所有点
    V.add(item[0])
    V.add(item[1])
A={}
p={}
for i in V:                      #初始化A和p
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
if s in Z:                  #先访问s点
    for i in Z[s]:
        A[i]=Z[s][i]
        p[i]=s
for i in V:                 #记录s点邻边的信息
    if A[i]!=100000000:
        flag=[p[i],i,A[i]]
        bucket.insert(B,flag,num)
        left=left+1
X.add(s)
A[s]=0
while(V-X and left):           #循环终止条件，V中的所有点都找到了最短路或者堆里面没有元素了，其中left记录的是堆里面元素剩余个数
    m=bucket.findmin(B,location,num)     #取桶中最小值
    left=left-1
    while m[1] in X:
        m=bucket.findmin(B,location,num)
        left=left-1
    X.add(m[1])
    if (m[1] in Z):
        for i in Z[m[1]]:           #点m[1]的邻边满足dijkstra条件，则将更新A值，记录p值，将这条边加入桶中
            if A[i]>A[m[1]]+Z[m[1]][i]:
                A[i]=A[m[1]]+Z[m[1]][i]
                flag=[m[1],i,A[i]]
                p[i]=m[1]
                bucket.insert(B,flag,num)
                left=left+1

for i in V:          #后面都是输出格式
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