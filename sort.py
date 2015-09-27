#!/usr/bin/python
# coding:utf-8
# Filename:sort.py

#1.插入排序={稳定:[直接插入,折半插入排序,2路插入排序],不稳定:[希尔排序]}
def InsertSort(li):
    for i in xrange(1,len(li)):
        for j in xrange(i-1,-1,-1):
            if li[j+1]<li[j]:
                tmp = li[j]
                li[j] =  li[j+1]
                li[j+1] = tmp
            else:
                break
#2.交换排序={稳定:[冒泡排序],不稳定:[快速排序]}
def ExchangeSort(li):
    exchange=len(li)-1
    while exchange>0:
        count=exchange
        exchange=0
        for i in xrange(count):
            if li[i]>li[i+1]:
                tmp=li[i+1]
                li[i+1]=li[i]
                li[i]=tmp
                exchange=i
#2.1交换排序:快速排序:先从后面选一个，再从前面选一个，交换，直到low=high，交换index=0的元素和index=low=high的元素，再递归。
def FastSort(li,low=0,high=0):
    if low<high:
        index_start,index_end=low,high
        mid=li[low]
        while low!=high:
            while low<high and li[high]>=mid:
                high-=1
            while low<high and li[low]<=mid:
                low+=1
            if low<high:
                tmp=li[low]
                li[low]=li[high]
                li[high]=tmp
        index_now=low
        li[index_start]=li[index_now]
        li[index_now]=mid
        FastSort(li,index_start,index_now-1)
        FastSort(li,index_now+1,index_end)
    else:
        pass
#3.选择排序
def ChooseSort(li):
    for i in xrange(len(li)-1,0,-1):
        key=i
        for j in xrange(i):
            if li[j]>li[key]:
                key=j
        if key!=i:
            tmp=li[i]
            li[i]=li[key]
            li[key]=tmp
#3.选择排序之堆排序：最坏时间复杂度为nlogn，空间O(1)，不稳定
def HeapSort(li,n):
    def Heapify(li,heapSize,index):
        left=2*index+1
        right = left + 1
        large = index
        if right < heapSize and li[large]<li[right]:
            large=right
        if left < heapSize and li[large]<li[left]:
            large=left
        if large != index:
            li[large],li[index]=li[index],li[large]
            Heapify(li,heapSize,large)
    def BuildMaxHeap(li):
        heapSize=len(li)
        for i in range(heapSize/2-1,-1,-1):
            Heapify(li,heapSize,i)
    BuildMaxHeap(li)
    heapSize=len(li)
    for i in range(heapSize-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        Heapify(li,i,0)

        
        
            
if __name__ == "__main__":
    #li=[1,3,5,7,9,8,6,4,2,0]
    #InsertSort(li)
    #li=[2,1,5,6,7,0,8,9,4,3]
    #ExchangeSort(li)
    #L=[6,1,7,5,3,9,0,8,2]
    #FastSort(L,0,len(L)-1)
    #li=[1,3,5,7,9,8,6,4,2,0]
    #ChooseSort(li)
    li=[1,3,5,7,9,8,6,4,2,0]
    HeapSort(li,len(li))
    print li
            
