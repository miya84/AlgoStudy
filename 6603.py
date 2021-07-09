

def combinations(n:list, r:int):
    output = []
    def backtrack(index, cur=[]):
        if len(cur) == r:
            print(' '.join(map(str,cur)))
        for i in range(index, len(n)):
            cur.append(n[i])
            backtrack(i+1, cur)
            cur.pop()
        
    backtrack(0, [])

    return output

# combinations([1, 2, 3, 5, 8, 13, 21, 34], 6)


while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    combinations(a[1:], 6)
    print()