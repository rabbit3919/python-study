from collections import deque  #데크를 사용하기 위해 import 

def solution(nums,k):
    answer=deque(nums)   # 데크는 O(1)로 접근 가능 , 일반적인 리스트는 O(n) 소요

    for i in range(k):
        answer.append(answer.popleft())
        #deque.method 
            #append : item을 데크의 오른쪽 끝에 삽입
            #appendleft : item을 데크의 왼쪽 끝에 삽입 
            #pop : 데크의 오른쪽 끝을 가져오고 동시에 데크에서 삭제
            #popleft : 데크의 왼쪽 끝을 가져오고 동시에 데크에서 삭제 
            #extend(array) : 주어진 배열을 순환하면서 데크의 오른쪽에 추가 
            #extendleft(array) : 주어진 배열을 순환하면서 왼쪽에 추가 
            #remove(item) : item을 데크에서 찾아 삭제 
            #rotate(num) : 데크를 num만큼 회전 ( 양수면 오른쪽, 음수면 왼쪽 )

    print("new array ",answer)


print(solution([3,7,1,5,9,2,8],3))
print(solution([2,12,2,1,3,3,9],2))
print(solution([1,2,5,4,6,7,9],6))
print(solution([1,3,6,8,14,2,1,7],5))
               

