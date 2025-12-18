class Vertex:
    def __init__(self, lv = None, rv = None, l = None, r = None, lc = 0, rc = 0, length = 0, best = 0):
        self.lv = lv
        self.rv = rv
        self.l = l
        self.r = r
        self.lc = lc
        self.rc = rc
        self.best = best
        self.len = length
    
def union(L, R):
    if L is None:
        return R
    if R is None:
        return L
        
    united = Vertex()
    united.len = L.len + R.len
    united.lv = L.lv
    united.rv = R.rv

    if (L.lc == L.len) and L.lv == R.lv:
        united.lc = L.lc + R.lc
    else:
        united.lc = L.lc
        
    if R.rc == R.len and L.rv == R.rv:
        united.rc = R.rc + L.rc
    else:
        united.rc = R.rc

    united.best = max(L.best, R.best)
    if R.lv == L.rv:
        united.best = max(united.best, R.lc + L.rc)
        
    return united
    
def build(a, tl, tr):
    if tl == tr:
        return Vertex(
            lv = a[tl],
            rv = a[tl],
            lc = 1,
            rc = 1,
            best = 1,
            length = 1
        )
    tm = (tl + tr) // 2
    left = build(a, tl, tm)
    right = build(a, tm + 1, tr)
    v = union(left, right)
    v.l = left
    v.r = right
    return v
        
def get_otvet(t, tl, tr, l, r):
    if l > r:
        return None
    if l == tl and tr == r:
        return t

    tm = (tl + tr) // 2
    return union(
        get_otvet(t.l, tl, tm, l, min(r, tm)),
        get_otvet(t.r, tm + 1, tr, max(l, tm + 1), r)
    )

K = int(input())
for p in range(K):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    root = build(a, 0, n-1)
    for _ in range(q):
        i , j = map(int, input().split())
        print(get_otvet(root, 0, n-1, i-1, j-1).best)