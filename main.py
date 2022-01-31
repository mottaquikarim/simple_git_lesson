import sys

if __name__ == '__main__':
    print(sys.argv)
    # drop the first item in list which is just the
    # name of file invoked
    args = sys.argv[1:]

    '''
    quadratic formula is:
        x = (-b + sqrt(b**2 - 4*a*c))/2a
        x = (-b - sqrt(b**2 - 4*a*c))/2a
    '''
    a = None
    b = None
    c = None

    # arg => a=1, then b=5, then c=6
    for arg in args:
        # left will be "a", right will be "1"
        left, right = arg.split("=")

        if left == 'a':
            # args are always string so cast it
            a = int(right)
        if left == 'b':
            b = int(right)
        if left == 'c':
            c = int(right)

    if None in [a,b,c]:
        raise Exception(f"a, b, c => {a}, {b}, {c}; cannot be None")

    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print(x1, x2)
