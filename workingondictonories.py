def find_it(seq):

    my_dict = {i:seq.count(i) for i in seq}
    for s in seq:
        if my_dict.get(s) % 2 != 0:
            return s
