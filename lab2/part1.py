r1 = [
 [1, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1],
 [0, 0, 1, 1, 1, 0],
 [0, 0, 1, 1, 1, 0],
 [0, 0, 1, 1, 1, 0],
 [0, 1, 1, 1, 1, 1],
]

r2 = [
 [1, 1, 0, 0, 1, 0],
 [0, 1, 0, 1, 0, 1],
 [0, 0, 1, 1, 0, 0],
 [1, 1, 1, 0, 1, 1],
 [0, 1, 1, 0, 1, 0],
 [1, 1, 0, 1, 0, 1],
]

r3 = [
 [1, 0, 1, 1, 0, 0],
 [0, 1, 0, 0, 0, 1],
 [1, 0, 1, 1, 0, 0],
 [1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 1],
]

r4 = [
 [1, 1, 1, 1, 1, 0],
 [0, 1, 1, 0, 1, 0],
 [0, 0, 1, 0, 0, 0],
 [0, 1, 1, 1, 1, 0],
 [0, 0, 1, 0, 1, 0],
 [1, 1, 1, 1, 1, 1],
]

r5 = [
 [0, 1, 0, 1, 1, 0],
 [0, 0, 0, 0, 0, 0],
 [1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 1, 0, 1, 1, 0],
]

r6 = [
 [0, 1, 1, 1, 1, 0],
 [0, 1, 0, 0, 1, 1],
 [0, 1, 0, 0, 0, 1],
 [0, 0, 1, 1, 0, 0],
 [1, 0, 1, 0, 0, 0],
 [0, 1, 0, 1, 0, 1],
]

r7 = [
 [0, 0, 0, 1, 0, 1],
 [1, 0, 0, 1, 0, 1],
 [1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 0, 1],
 [1, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0],
]

r8 = [
 [0, 0, 0, 0, 0, 0],
 [1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 0],
]

def asymmetric(relation):
    for i in range(0, len(relation)):
        for j in range(i, len(relation)):
            if relation[i][j] and relation[j][i]:
                return False
    return True

def get_dominators_by_P(relation):
    dominators = []
    for i, row in enumerate(r):
        if all([x == 1 for x in row[0:i] + row[i:-1]]):
            dominators.append(i + 1)
    return dominators

def get_dominators_by_R(relation):
    dominators = []
    for i, row in enumerate(r):
        if  all([x == 1 for x in row]):
            dominators.append(i + 1)
    return dominators

def get_dominators_by_R_strict(relation):
    dominators = []
    for i, row in enumerate(r):
        if  all([x == 1 for x in row]):
            column = [col_row[i] for col_row in r]
            if all([y == 0 for y in column[0:i] + column[i:-1]]):
                dominators.append(i + 1)
    return dominators

def get_blockers_by_P(relation):
    blockers = []
    for j in range(0, len(relation)):
        is_blocker = True
        for i in range(0, len(relation)):
            if relation[i][j] != 0:
                is_blocker = False
                break
        if is_blocker:
            blockers.append(j + 1)
    return blockers

def get_blockers_by_R(relation):
    blockers = []
    for j in range(0, len(relation)):
        is_blocker = True
        for i in range(0, len(relation)):
            if relation[i][j] != 0 and relation[j][i] != 1:
                is_blocker = False
                break
        if is_blocker:
            blockers.append(j + 1)
    return blockers

def get_blockers_by_R_strict(relation):
    blockers = []
    for j in range(0, len(relation)):
        is_blocker = True
        for i in range(0, len(relation)):
            if relation[i][j] != 0 and j != i:
                is_blocker = False
                break
        if is_blocker:
            blockers.append(j + 1)
    return blockers

relations = [r1, r2, r3, r4, r5, r6, r7, r8]

for i, r in enumerate(relations):
    if asymmetric(r):
        print(str(i + 1) + ' is asymmetric')
        print("Dominators for r" + str(i + 1) + " by P " + str(get_dominators_by_P(r)))
        print("Blockers for r" + str(i + 1) + " by P " + str(get_blockers_by_P(r)))
    else:
        print(str(i + 1) + ' is symmetric')
        print("Dominators for r" + str(i + 1) + " by R " + str(get_dominators_by_R(r)))
        print("Dominators for r" + str(i + 1) + " by R strict " + str(get_dominators_by_R_strict(r)))
        print("Blockers for r" + str(i + 1) + " by R " + str(get_blockers_by_R(r)))
        print("Blockers for r" + str(i + 1) + " by R strict " + str(get_blockers_by_R_strict(r)))
    print('---------------------------------------------------')
