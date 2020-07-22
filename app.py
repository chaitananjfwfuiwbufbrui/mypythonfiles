
def digital_root(n):
    a = list(map(int, ' '.join(str(n)).split()))
    z = 0
    for i in a:
        z = z + i

    if z > 10:
        return digital_root(z)

    else:
        return z
n = int(input("enter 6thge number"))




