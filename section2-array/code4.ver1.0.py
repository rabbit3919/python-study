def solution(nums,k):
    listsize=len(nums)                       # 배열 길이 받아오기
    new_list=[0 for i in range(listsize)]    # 배열의 길이만큼 새로운 리스트 초기화 
    
    for i in range(k,listsize):             # k index부터 배열의 길이만큼은 
        new_list[i-k]=nums[i]               # 새로운 배열의 0번째 index부터 채우기 
        #print("i,listsize-1-i ",i-k,i)
        
              
    for i in range(0,k):                    # 원래 기존 배열의 0 ~ k index부터의 값은
        new_list[listsize-k+i]=nums[i]      # 배열의 길이 - 입력받은 k + 1의 index부터 채우기 
        #print("listsize-k+1,i ",listsize-k+i,i)

    print("new array ",new_list)


print(solution([3,7,1,5,9,2,8],3))
print(solution([2,12,2,1,3,3,9],2))
print(solution([1,2,5,4,6,7,9],6))
print(solution([1,3,6,8,14,2,1,7],5))
               

