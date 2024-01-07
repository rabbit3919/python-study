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

def solution(nums):
    listsize=len(nums)
    answer=deque()

    answer.appendleft(nums[0])

    for i in range(1,listsize):
        if nums[i-1] != nums[i]:
            answer.appendleft(nums[i])

    return list(answer)

    
print(solution([0,1,1,1,2,2,2,3]))