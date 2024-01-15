def solution():
    sh = dict()
    sh={'a': 3, 'b':5,'c': 2}

    for key in sh:
        print(key)


    for key in sh.values():
        print(key)

    
    for key,val in sh.items():
        print(key, val)


    p1='a' in sh;
    
    print(p1)

    del sh['a']
    print(sh)

    print(len(sh))

solution()

