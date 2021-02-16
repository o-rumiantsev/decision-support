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

def reflexive(relation):
    for i, row in enumerate(relation):
        if (row[i] == 0):
            return False
    return True

def irreflexive(relation):
    for i, row in enumerate(relation):
        if (row[i] == 1):
            return False
    return True

def symmetric(relation):
    for i in range(0, len(relation)):
        for j in range(i, len(relation)):
            if relation[i][j] ^ relation[j][i]:
                return False
    return True

def asymmetric(relation):
    for i in range(0, len(relation)):
        for j in range(i, len(relation)):
            if relation[i][j] and relation[j][i]:
                return False
    return True

def antisymmetric(relation):
    for i in range(0, len(relation)):
        for j in range(i + 1, len(relation)):
            if relation[i][j] and relation[j][i]:
                return False
    return True

def transitive(relation):
    for i in range(0, len(relation)):
        for j in range(0, len(relation)):
            if relation[i][j] == 1:
                for k in range(0, len(relation)):
                    if relation[j][k] == 1 and relation[i][k] != 1:
                        return False
    return True

def negatively_transitive(relation):
    for i in range(0, len(relation)):
        for j in range(0, len(relation)):
            if relation[i][j] == 0:
                for k in range(0, len(relation)):
                    if relation[j][k] == 0 and relation[i][k] != 0:
                        return False
    return True

def linked(relation):
    for i in range(0, len(relation)):
        for j in range(i, len(relation)):
            if not (relation[i][j] or relation[j][i]):
                return False
    return True

def weakly_linked(relation):
    for i in range(0, len(relation)):
        for j in range(i + 1, len(relation)):
            if not (relation[i][j] or relation[j][i]):
                return False
    return True

def check_cycle(relation, k, i, path=[]):
    for j in range(len(relation)):
        if relation[k][j] == 1 and not (j in path):
            if relation[j][i] == 1 or check_cycle(relation, j, i, path + [j]):
                return True


def acyclic(relation):
    if not irreflexive(relation):
        return False

    if symmetric(relation):
        return False

    for i in range(len(relation)):
        if check_cycle(relation, i, i):
            return False

    return True

classes = {
    'strict order': [irreflexive, asymmetric, transitive, acyclic],
    'non-strict order': [reflexive, antisymmetric, transitive],
    'weak ordering': [asymmetric, transitive, negatively_transitive],
    'equivalence': [reflexive, symmetric, transitive],
    'quasi order': [reflexive, transitive],
    'tolerance': [reflexive, symmetric],
}

relations = [r1, r2, r3, r4, r5, r6, r7, r8]
results = []

for r in relations:
    r_props = []
    for class_name in classes:
        properties = classes[class_name]
        if all(property(r) for property in properties):
            r_props.append(class_name)
            break
    results.append(r_props)

print(results)
