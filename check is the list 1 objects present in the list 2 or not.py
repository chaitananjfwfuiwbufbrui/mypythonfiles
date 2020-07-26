def scramble(s1, s2):
    z = [ p for p in s2]
    s = [ i  for i in s1]
    check = all(item in s for item in z)
    if check == True:
        return True
    else:
        return False
    # your code here

print(scramble('nm b n', 'world'))
