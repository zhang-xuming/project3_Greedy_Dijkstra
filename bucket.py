def built_bucket(num):               #建立num个桶
    B=[[] for i in range(num) ]
    return B

def insert(B,flag,num):             #根据权重的mod(num)值，循环利用桶，将边插入对应下标桶中
    i=flag[2]%num
    B[i].append(flag)

def findmin(B,location,num):        #根据下标，找桶中最小的值，将下标加1再mod(num),返回最小边
    while not B[location[0]]:
        location[0]=(location[0]+1)%num
    L=B[location[0]].pop(0)
    return L

