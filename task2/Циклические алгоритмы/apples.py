from operator import floordiv, mul
from itertools import tee, accumulate, repeat, product

types = (15, 17, 21)
n = 185

variants = (map(mul, range(n//t + 1), repeat(t)) for t in types)
count = filter(lambda x: sum(x) == n, product(*variants))
to_len, result = tee(map(floordiv, c, types) for c in count)

print(sum(1 for _ in to_len))
for r in result:
    print(*r)