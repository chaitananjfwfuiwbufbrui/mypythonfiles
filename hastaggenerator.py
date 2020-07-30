def generate_hashtag(s):

    z = s.title()
    p = z.split(" ")

    c = ""

    if len( c.join(p)) == 0:
        return False
    elif len(c.join(p)) > 140:
        return False
    else:
        return '#' + c.join(p)
