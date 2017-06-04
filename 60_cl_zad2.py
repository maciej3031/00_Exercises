class Tree(object):
    x = 0
    l = None
    r = None

    def __init__(self, x, l, r):
        self.x = x
        self.l = l
        self.r = r

T = Tree(4, Tree(5, Tree(4, Tree(5, None, None), None), None), Tree(6, Tree(1, None, None), Tree(6, None, None)))

path = []
res = []


def solution(T):
    def function(T):
        if T.x not in path:
            path.append(T.x)
            if T.l:
                solution(T.l)
            if T.r:
                solution(T.r)
        else:
            temp = len(path)
            path.pop(-1)
            res.append(temp)
    function(T)
    return max(res)

print(solution(T))
