#!/usr/bin/python
# coding:utf-8
# Filename:search.py


def search_bin(li,key):
    low,high=0,len(li)-1
    result=-1
    while low<=high:
        mid=(low+high)/2
        if key==li[mid]:
            result=mid
            break
        elif key<li[mid]:
            high=mid-1
        else:
            low=low+1
    return result







if __name__ == '__main__':
    li=range(10)
    print search_bin(li,3)
    print search_bin(li,9)
    print search_bin(li,20)
