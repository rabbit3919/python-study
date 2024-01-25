def solution(nums):
    answer=0
    n=len(nums)

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for i in range(n):
        for j in range(n):
            flag=True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nums[i][j] >= nums[nx][ny]:
                    flag = False
                    break
            if flag == True:
                answer += 1
    
    return answer