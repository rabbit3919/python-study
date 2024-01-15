from collections import Counter

def solution(s):
    list=Counter(s)

    odd=0

    for key in list:
        if list[key] % 2 == 1:
            odd += 1


    return len(s) - odd + 1 if odd > 0 else len(s)

print(solution("abcbbbccaaeee"))