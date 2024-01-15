def solution(nums):
    answer=-1

    cnt = [0] * 1001

    for x in nums:
        cnt[x] += 1


    for i in range(len(cnt)-1,0,-1):
        if cnt[i] == 1:
            return i
        
    


print(solution([3,9,2]))