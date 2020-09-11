"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#  q = set(range(1, 10))
q = set(range(1, 2000))
#  q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sumdiff(q):
    left_sides = {}
    for a in q:
        for b in q:
            left_sides[f(a) + f(b)] = (a, b)

    solution_count = 0
    for c in q:
        for d in q:
            right_side = f(c) - f(d)
            if right_side in left_sides:
                solution_count += 1
                #  a = left_sides[right_side][0]
                #  b = left_sides[right_side][1]
                #  function_string = f'f({a}) + f({b}) = f({c}) - f({d})'
                #  number_string = f'{f(a)} + {f(b)} = {f(c)} - {f(d)}'
                #  print(function_string + '\t' + number_string)
    print("Solution Count: ", solution_count)


sumdiff(q)
