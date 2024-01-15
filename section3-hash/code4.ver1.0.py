from collections import defaultdict
from collections import Counter

def solution(s):
    list = Counter(s)
    odd = 0 

    for key in list:
        if list[key] % 2 == 1:
            odd += 1
        
    if odd <= 1:
        return True
    else:
        return False



print(solution("abc"))
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))