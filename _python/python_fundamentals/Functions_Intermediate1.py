import random
def randInt(min=0, max =100):
    num = 0
    if min <= max and max > 0:
        num = round(random.random() *(max-min) + min)
    return num


print(randInt())