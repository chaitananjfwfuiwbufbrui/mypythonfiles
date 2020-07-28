def rgb(r, g, b):
    m = 0
    i = 255
    def red(a):
        x = hex(a)
        if a < 0:
            return  red(m)
        elif a < 10:
            return x.replace(x[1],"")
        elif a > 255:
           return red(i)
        else:
             return  x[-2:]
    def green(a):
        o = hex(a)
        if a < 0:
            return green(m)

        elif a < 10:
            return o.replace(o[1],"")
        elif a > 255:
            return green(i)
        else:
             return  o[-2:]
    def blue(a):
        p = hex(a)
        if a < 0:
            return blue(m)
        elif a < 10:
            return p.replace( p[1],"")
        elif a > 255:
            return blue(i)
        else:
             return  p[-2:]

    s =  red(r) + green(g) + blue(b)

    return s.upper()
