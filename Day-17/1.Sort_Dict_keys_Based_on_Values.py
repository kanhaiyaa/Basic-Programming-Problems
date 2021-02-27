#[p1: 10, p2:8, p3:12] sort keys based on values like [p2, p1, p3]

d = {'p1':10, 'p2':8, 'p3':12}
sorted(d, key=lambda k: d[k])