
def spin_words(sentence):

    n = sentence.split()

    for i in range(len(n)):
        if len(n[i]) < 5:
            return  n[i]

        else:
            x = n[i]
            string = "".join(reversed(x))
            return string



word = "dopr kup plungsg etriebe"
print(spin_words(word))

