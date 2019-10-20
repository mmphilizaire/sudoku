
groups=[[0,0,0] for x in range(81)]

rows = [[] for x in range(9)]
cols = [[] for x in range(9)]
for num in range(81):
    rows[num//9].append(num)
    groups[num][0]=num//9
    cols[num%9].append(num)
    groups[num][1]=num%9
box = [[] for x in range(9)]
pos = 0
for r1 in range(0,3):
    for c1 in range(0,3):
        start = [r1*3,c1*3]
        for r2 in range(start[0],start[0]+3):
            for c2 in range(start[1],start[1]+3):
                index = r2+c2*9
                box[pos].append(index)
                groups[index][2]=pos
        pos+=1

lookup=[[] for x in range(81)]
for group in rows+cols+box:
    for i in group:
        for x in group:
            if x != i:
                lookup[i].append(x)
for index in range(len(lookup)):
    lookup[index]=set(lookup[index])

def poss1(pzl,index):
    poss = []
    nums = "123456789"
    for num in nums:
        can = True
        for x in lookup[index]:
            if pzl[x]==num:
                can = False
                break
        if can: poss.append(num)
    return poss

def bruteforce(pzl,indeces):
    if not indeces: return pzl
    index = 0
    for x in range(len(indeces)):
        if len(indeces[x][1])<len(indeces[index][1]):
            index = x
    for possib in indeces[index][1]:
        temp = [row[:] for row in indeces]
        for empty in temp:
            if empty[0] in lookup[temp[index][0]]:
                if possib in empty[1]:
                    empty[1] = empty[1][:empty[1].index(possib)]+empty[1][empty[1].index(possib)+1:]
        newpzl = pzl[:temp[index][0]]+possib+pzl[temp[index][0]+1:]
        bf = bruteforce(newpzl,(temp[:index]+temp[index+1:]))
        if bf!=[]: return bf
    return []

def display(pzl):
    for x in range(9):
        line = ""
        for y in range(9):
            line = line+(pzl[9*x+y])+" "
        print(line)

puzzles = open("sud.txt","r")
count = 1
for line in puzzles:
    if count < 129:
        print("puzzle %s" % count)
        sud = line
        indeces = [[x,poss1(sud,x)] for x in range(len(sud)) if sud[x]=="."]
        sol = bruteforce(sud,indeces,)
        if sol == []: print("no solution")
        else:
            print("solution: ")
            display(sol)
            sum1 = sum([int(x) for x in sol.rstrip("\n")])
            print(sum1)
        print("")
    count+=1
