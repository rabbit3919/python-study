# 매개변수 k에 합격 커트라인 점수보다 높은 학생 수 구하기
def solution(score,k):
    listsize=len(score)   #배열 길이 받아오기
    count=0               #학생 수를 담을 count

    for i in range(0,listsize): # 배열 길이만큼 for문 돌기
        if int(score[i]) >= k:  # k보다 높으면 
            count=count+1       # count에 +1


    print("answer is ",count)


print(solution([60,50,80,90,55,70,65,45],60))
print(solution([10,20,30,40,50],60))
print(solution([50,65,75,87,90,55,78,93,100],70))
print(solution([99,30,50,55,68,70,90,100],80))