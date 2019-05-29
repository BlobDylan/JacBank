import random


def generate(small, capital, numbers, chars):
    p = ''
    length = random.randint(20,25)
    for i in range(length):
        x = []
        if small:
            x.append(str(chr(random.randint(97, 122))))
        if capital:
            x.append(str(chr(random.randint(65,90))))
        if numbers:
            x.append(str(random.randint(0,9)))
        if chars:
            ch = []
            ch.append(str(chr(random.randint(123, 126))))
            ch.append(str(chr(random.randint(33,47))))
            ch.append(str(chr(random.randint(58,64))))
            ch.append(str(chr(random.randint(91,96))))
            x.append(random.choice(ch))
        p += random.choice(x)
    return p
