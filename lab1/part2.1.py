from graphviz import Digraph

dot = Digraph()

r = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
]

# Строгий порядок
r1 = [
    [0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
]

#  Нестрогий порядок
r2 = [
    [1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 1],
]

def render(relation, filename):
    dot = Digraph(format='png')
    for i in range(len(relation)):
        for j in range(len(relation)):
            if relation[i][j]:
                dot.edge(str(i + 1), str(j + 1))
    dot.render(filename, view=True)

render(r2, 'relation')
# render(r2, 'relation2')

def transitive(relation):
    for i in range(0, len(relation)):
        for j in range(0, len(relation)):
            if relation[i][j] == 1:
                for k in range(0, len(relation)):
                    if relation[j][k] == 1 and relation[i][k] != 1:
                        return False
    return True
