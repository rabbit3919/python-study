from collections import defaultdict

def solutions(participant,completion):
    # 참가자의 이름을 dictionary에 넣기 
    list=defaultdict(int)
    answer=defaultdict(int)
    check=defaultdict(int)
    flag=0

    for i in range(0,len(participant)):
        list[i]=participant[i]

    for key in list:
        #print(list[key]) - a / b / c
        for i in range(0,len(completion)):
            if list[key] == completion[i]:
                flag=1
                check[i]=True
                exit
        if flag == 1:
            answer[key]=True
        else:
            answer[key]=False
        flag=0

    print(check)
    for key in answer:
        if answer[key] == False:
            if check[key] != True:
                print(participant[key])

    
# leo   leo    kiki    /    leo kiki 
# true  
       
print(solutions(['leo','eden','eden'],['eden','leo']))