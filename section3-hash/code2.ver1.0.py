from collections import defaultdict

def solutions(nums):
    answer = -1

    list=defaultdict(int)

    for i in nums:
        list[i]+=1

    
    for key in list:
        if list[key] == 1:
            answer=max(answer,key)

    return answer


print(solutions([3,9,2,12,9,12,8,7,9,12]))

