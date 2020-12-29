import random
def daily_stoic():
    afile = open('quotes.txt', "r")
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
    return str(line)