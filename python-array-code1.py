# 수열의 원소에서 가장 작은 값을 찾을 때 
# 매개변수 num에 길이가 n / 수열의 원소 중 가장 작은 값을 찾기 

min=0
list=[80,90,25,27,30]  # 배열의 index는 0,1,2,3,4~

read=input()    # n을 input으로 받기
n=int(read)-1   # input으로 받는 경우 str이기 때문에 int로 변환 후 -1
                # -1을 해주는 이유는 index는 0부터 시작이기 때문

min=list[0]     # 최솟값을 배열 0번째 index로 설정

# if 배열의 길이가 5일때 n=5
for i in range(1,n):
  if min > list[i]:
    min=list[i]
    

print("minimun value is ",min)
