w, h = map(int, input().split())
t = eval(repr([[0]*h]*w))
ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
e = x = y = d = 0
for i in range(w*h):
    t[x][y] = i
    if x+ds[d][0] in [e-1-(1 if d == 3 else 0), w-e] or y+ds[d][1] in [e-1, h-e]:
        d = (d+1) % 4
        e += d//3
    x, y = map(sum, zip(ds[d], [x, y]))
for i in range(w*h):
    print(("%%%dd" % (len(str(w*h-1))+1)) %
          t[i % w][i//w], end=('\n' if i % w == w-1 else ''))
