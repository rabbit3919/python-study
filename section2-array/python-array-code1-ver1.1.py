# 수열의 원소에서 가장 작은 값을 찾을 때 
# 매개변수 num에 길이가 n / 수열의 원소 중 가장 작은 값을 찾기 

def solution(list):
  #list는 배열 입력 
  listsize=len(list) #배열 사이즈 구하기 
  min=list[0]        #최솟값을 배열의 0번째 값으로 설정


  
  for i in range(1,listsize):
    if min > list[i]:  #설정한 min 값이 배열의 값보다 크면  
      min=list[i]      #배열의 값을 min으로 설정
      min_indx=i

  print("minimun index value is ",min_indx)


print(solution([7,10,5,3,2,15,19]))
print(solution([-12,12,30,-15,-5,3,9,-11,14]))
print(solution([17,11,5,8,23,29,19,12,25,16,-2]))
print(solution([7,5,12,-9,-12,22,-30,-35,-21]))