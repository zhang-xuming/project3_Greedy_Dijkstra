import math
def heap_insert(A,edge):
    A.append(edge)                 #将新的边插入堆的最后
    i=len(A)-1
    while i>0 and A[math.ceil(i/2)-1][2]>A[i][2]:             #新加的边从堆的最后向上冒泡
        A[i],A[math.ceil(i/2)-1]=A[math.ceil(i/2)-1],A[i]
        i=math.ceil(i/2)-1

def min_heapify(A,i):            #维护堆，向下冒泡
    l=2*i+1
    r=2*i+2
    if l<=len(A)-1 and A[l][2]<A[i][2]:       #将i节点与其左节点相比较
        minimum=l
    else :minimum=i
    if r<=len(A)-1 and A[r][2]<A[minimum][2]:  #将minimun节点与i的右节点相比较
        minimum=r
    if minimum !=i:
        A[i],A[minimum]=A[minimum],A[i]      #节点i与节点minimum换位
        min_heapify(A,minimum)          #递归维护

def extract_min(A):
    min=A.pop(0)               #取堆中最小值
    if len(A)>0:
        A.insert(0,A.pop())     #将最后一个叶子插入堆的开头
        min_heapify(A,0)        #维护堆
    return min




