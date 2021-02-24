from graphviz import Digraph

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

def render(relation, title, filename):
    dot = Digraph(title, format='png')
    for i in range(len(relation)):
        for j in range(len(relation)):
            if relation[i][j]:
                dot.edge(str(i + 1), str(j + 1))
    dot.render(filename, view=True)

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
    'Strict order': [irreflexive, asymmetric, transitive, acyclic],
    'Non-strict order': [reflexive, antisymmetric, transitive],
    'Weak ordering': [asymmetric, transitive, negatively_transitive],
    'Equivalence': [reflexive, symmetric, transitive],
    'Quasi order': [reflexive, transitive],
    'Tolerance': [reflexive, symmetric],
}

relations = [r1, r2, r3, r4, r5, r6, r7, r8]

# for i, r in enumerate(relations):
#     r_props = []
#     no_class = True
#     for class_name in classes:
#         properties = classes[class_name]
#         if all(property(r) for property in properties):
#             no_class = False
#             print(i, class_name)
# #             render(r, class_name, 'r' + str(i + 1))
#             break
#     if no_class:
#         print(i, 'no class')
# #         render(r, 'No class', 'r' + str(i + 1))


properties = {
    reflexive: 'reflexive',
    irreflexive: 'irreflexive',
    symmetric: 'symmetric',
    asymmetric: 'asymmetric',
    antisymmetric: 'antisymmetric',
    transitive: 'transitive',
    negatively_transitive: 'negatively_transitive',
    linked: 'linked',
    weakly_linked: 'weakly_linked',
    acyclic: 'acyclic',
}

for i, r in enumerate(relations):
    props = []
    for prop in properties:
        if prop(r):
            props.append(properties[prop])
    print(i, props)