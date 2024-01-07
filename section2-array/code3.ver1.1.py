# 매개변수 nums에 0과 1로된 수열이 주어지면 
# 1이 연속된 부분수열 중 가장 긴 부분수열의 길이를 반환하는 프로그램을 작성

def solution(nums):
    listsize=len(nums)      # 배열 길이 받아옴
    answer=0                # 정답 변수 ( 부분수열 중 1이 없을수도 있기 때문에 0으로 초기화 )
    count=0                 # count 변수 

    for i in range(0,listsize):         # 배열 길이만큼 for문 돌기 
        if nums[i]==1:                  # 배열의 값이 1이면 
            count+=1                    # count=count+1
        else:                           # 배열의 값이 1이 아닐때, 0이라면 
            if answer < count:          # answer보다 count했던 값이 크다면 
                answer=count            # 해당 값을 answer 
            count=0                     # 0을 만났으니 count값을 0으로 다시 초기화 
    answer = max(answer,count)
    print("answer is ",answer)


print(solution([1,1,0,1,1,1,0,1,1,1,1,1]))
print(solution([0,0,1,0,1,0,0]))
print(solution([1,1,1,1,1]))
print(solution([1,0,1,1,0,1,1,1,0,1,1,1,0,1]))


    