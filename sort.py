import random

#交换排序
## 1. 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)):
        exchange_flag=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                exchange_flag=True
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
        if not exchange_flag:
            break
    return arr
## 2. 快速排序
def quick_sort(arr,low,high):#递归方法
    def partition(arr,low,high):
        middle=low#中轴元素
        flag=True
        index=high
        while low<high:
            if arr[middle]<arr[high] and flag:
                high-=1
                index=high
                continue
            if arr[middle]>arr[low] and not flag:
                low+=1
                index=low
                continue
            flag=not flag
            tmp=arr[index]
            arr[index]=arr[middle]
            arr[middle]=tmp
            middle=index
        return middle
    if low>=high:
        return  arr
    middle=partition(arr,low,high)
    quick_sort(arr,low,middle-1)
    quick_sort(arr,middle+1,high)
    return arr


#插入排序
## 3. 直接插入排序
def insert_sort(arr):
    for i in range(1,len(arr)):
        tmp=arr[i]
        for j in reversed(range(i)):
            if tmp>arr[j]:
                arr[j+1]=tmp
                break
            else:
                arr[j+1]=arr[j]
            if j==0:
                arr[j]=tmp
    return arr
## 4. 希尔排序
def shell_sort(arr,hs):
    for h in hs:
        i=0
        while i<h:
            j=i
            index=j
            while j<len(arr):
                tmp=arr[j]
                for k in reversed(range(index,j,h)):
                    if tmp>arr[k]:
                        arr[k+h]=tmp 
                        break
                    else:
                        arr[k+h]=arr[k]
                    if k==index:
                        arr[k]=tmp
                j+=h
            i+=1
    return arr
    
#选择排序
## 5. 简单选择排序
def select_sort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        index=i
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                index=j
        if index!=i:
            tmp=arr[i]
            arr[i]=min
            arr[index]=tmp 
    return arr

## 6. 堆排序
def maxheap_sort(arr):
    def heap(arr):#建堆,自底向上
        i=len(arr)//2-1
        while i>=0:
            if 2*i+2<len(arr):#有左右子树
                if arr[2*i+1]>arr[2*i+2]:
                    if arr[i]>=arr[2*i+1]:
                        i-=1
                    else:   
                        tmp=arr[i]
                        arr[i]=arr[2*i+1]
                        arr[2*i+1]=tmp 
                        i=2*i+1
                else:
                    if arr[i]>=arr[2*i+2]:
                        i-=1
                    else:   
                        tmp=arr[i]
                        arr[i]=arr[2*i+2]
                        arr[2*i+2]=tmp 
                        i=2*i+2
            elif 2*i+1<len(arr):#只有左子树
                if arr[i]>=arr[2*i+1]:
                    i-=1
                else:   
                    tmp=arr[i]
                    arr[i]=arr[2*i+1]
                    arr[2*i+1]=tmp 
                    i=2*i+1
            else:#叶子节点
                i=(i+1)//2-1
    def heapify(arr,end): #调整0~i为堆，自顶向下
        index=0
        while index<=(end+1)//2-1:
            if 2*index+2<=end:
                if arr[2*index+1]>arr[2*index+2]:
                    if arr[index]>=arr[2*index+1]:   
                        break 
                    else:
                        tmp=arr[index]
                        arr[index]=arr[2*index+1]
                        arr[2*index+1]=tmp 
                        index=2*index+1
                else:
                    if arr[index]>=arr[2*index+2]:
                        break 
                    else:
                        tmp=arr[index]
                        arr[index]=arr[2*index+2]
                        arr[2*index+2]=tmp
                        index=2*index+2
                
            elif 2*index+1<=end:
                if arr[index]>=arr[2*index+1]:
                    break 
                else:
                    tmp=arr[index]
                    arr[index]=arr[2*index+1]
                    arr[2*index+1]=tmp 
                    index=2*index+1

    heap(arr)
    tmp=arr[0]
    arr[0]=arr[-1]
    arr[-1]=tmp 
    for i in range(len(arr)-2,0,-1):
        heapify(arr,i)
        tmp=arr[0]
        arr[0]=arr[i]
        arr[i]=tmp 
    return arr

#7. 归并排序
def merge_sort(arr,start,end):
    def merge(arr1,arr2):
        res=[]
        i,j=0,0
        while i<len(arr1) or j<len(arr2):
            if i==len(arr1):
                res.extend(arr2[j:])
                break
            if j==len(arr2):
                res.extend(arr1[i:])
                break
            if arr1[i]<arr2[j]:
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        return res
    if start==end:
        return arr[start:end+1]
    middle=(start+end)//2
    arr1=merge_sort(arr,start,middle)
    arr2=merge_sort(arr,middle+1,end)
    return merge(arr1,arr2)
#8. 计数排序
def counting_sort(arr):
    max_num=max(arr)
    min_num=min(arr) 
    length=max_num-min_num+1 
    offset=-min_num #y=x+offset
    tmp=[0]*length
    for x in arr:
        tmp[x+offset]+=1
    arr=[]
    for y,count in enumerate(tmp):
        while count>0:
            arr.append(y-offset)
            count-=1
    return arr
#9. 基数排序
import math
def radix_sort(arr):
    max_num=max(arr)
    min_num=min(arr)
    max_num_length=len(str(max_num)) if max_num >=0 else len(str(max_num))-1
    min_num_length=len(str(min_num)) if min_num >=0 else len(str(min_num))-1
    length=max(max_num_length,min_num_length)
    counting=[0]*19#-9~9
    record=[[] for _ in range(19)]
    offset=9
    for i in range(length):
        for x in arr:
            index=(x//(10**i))%10 if x >=0 else (math.ceil(x/(10**i)))%10-10
            index=0 if index==-10 else index
            counting[index+offset]+=1
            record[index+offset].append(x)
        arr=[]
        for y,count in enumerate(counting):
            l=0
            while l<count:
                arr.append(record[y][l])
                l+=1
        counting=[0]*19
        record=[[] for _ in range(19)]
    return arr
#10. 桶排序
def bucket_sort(arr,bucket_num):
    max_num=max(arr)
    min_num=min(arr)
    length=max_num-min_num+1
    interval=length//bucket_num+1
    buckets=[[] for _ in range(bucket_num)]
    for x in arr:
        number=(x-min_num)//interval #桶的编号
        buckets[number].append(x)
        for i in range(len(buckets[number])-2,-1,-1):
            if buckets[number][i]<x:
                buckets[number][i+1]=x 
                break
            else:
                buckets[number][i+1]=buckets[number][i]
            if i==0:
                buckets[number][i]=x
    arr=[]
    for bucket in buckets:
        if len(bucket)>0:
            arr.extend(bucket)
    return arr

if __name__ == "__main__":
    mysort=radix_sort
    arr=[random.randint(-100,100) for i in range(100)]
    print(f"原数组:{arr}")
    sorted_arr=sorted(arr)
    mysorted_arr=mysort(arr)
    print(f"标准排序后数组:{sorted_arr}")
    print(f"我的排序后数组:{mysorted_arr}")
    if sorted_arr==mysorted_arr:
        print("排序正确")
    else:
        print("排序错误")
