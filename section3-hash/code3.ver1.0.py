from collections import defaultdict

def solutions(nums):
    answer = -1

    list=defaultdict(int)

    for i in nums:
        list[i]+=1

    for key,val in list.items():
        if key == val:
            return key
        
    return answer


print(solutions([1,2,3,1,3,3,2,4]))
print(solutions([1,2,3,3,3,2,4,5,5,5]))
print(solutions([1,1,2,5,5,5,5,5,3,3,3,3,5]))
print(solutions([7,6,7,7,8,8,8,8,7,5,7,7,7,8,8]))
print(solutions([11,12,5,5,3,11,7,12,15,12,12,11,12,12,7,8,12,11,12,7,12,5,15,20,15,12,15,12,15,14,12]))