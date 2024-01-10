from collections import deque

def solution():
    print("number input")
    num=input()
    list=[]
    count=1

    for i in range(0,int(num)):
        print("stick number input")
        stick=input()
        list.append(stick)

    last=list[int(num)-1]

    for i in range(0,int(num)):
        if list[i] > last:
            count=count+1

    return count

print(solution())