def find_next_square(sq):
    sqrt = sq ** 0.5
    if not sqrt.is_integer():
        return print(-1)
    else:
        while True:
            sq += 1
            sqrt = sq ** 0.5
            if sqrt.is_integer():
                break
        return print(sq)

find_next_square(121)
find_next_square(255)
