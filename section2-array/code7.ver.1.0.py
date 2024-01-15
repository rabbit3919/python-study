from collections import deque

def solution():
    print("number input")   # 막대기를 몇개를 넣을건지 
    num=input()             # input 함수로 변수 받기 
    list=[]                 # 변수를 받아서 넣을 list를 선언해주기 
    count=1                 # 결과적으로 반환하려는 count 값 변수를 1로 초기화 

    for i in range(0,int(num)):      # 막대기 갯수만큼 for문 돌기 
        print("stick number input")  
        stick=input()                # 막대기에 써져있는 숫자를 input 함수로 받기 
        list.append(stick)           # 써져있는 숫자를 append 함수를 통해서 list에 넣기 

    max=list[int(num)-1]            # list 마지막에 있는 숫자가 기준이 되어야 하니까 배열 마지막 수를 last에 넣어주기 

    # input = 5  int(num)
    #  r = 4 3 2 1 0    int(num)
    #  i =  1 2 3 4    5-i-1
    for i in range(1,int(num)):       
        if list[int(num)-i-1] > max:
            max=list[int(num)-i-1]
            count=count+1

    return count
    
print(solution())