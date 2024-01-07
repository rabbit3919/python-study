from collections import deque

        #deque.method 
            #append : item을 데크의 오른쪽 끝에 삽입
            #appendleft : item을 데크의 왼쪽 끝에 삽입 
            #pop : 데크의 오른쪽 끝을 가져오고 동시에 데크에서 삭제
            #popleft : 데크의 왼쪽 끝을 가져오고 동시에 데크에서 삭제 
            #extend(array) : 주어진 배열을 순환하면서 데크의 오른쪽에 추가 
            #extendleft(array) : 주어진 배열을 순환하면서 왼쪽에 추가 
            #remove(item) : item을 데크에서 찾아 삭제 
            #rotate(num) : 데크를 num만큼 회전 ( 양수면 오른쪽, 음수면 왼쪽 )

def solution(nums,target):
    answer=[0]*2
    listsize=len(nums)
    for i in range(0,listsize-1):
        for k in range(i+1,listsize):
            if nums[i] + nums[k] == target:
                return sorted([nums[i],nums[k]])
    
    return answer
    

print(solution([7,3,2,13,9,15,8,11],12))
print(solution([21,12,30,15,6,2,9,19,14],24))
print(solution([12,18,5,8,21,27,22,25,16,2],28))
print(solution([11,17,6,8,21,9,19,12,25,16,2],26))
print(solution([7,5,12,-9,-12,22,-30,-35,-21],-14))
print(solution([7,5,12,20],15))