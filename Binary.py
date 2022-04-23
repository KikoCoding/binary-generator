from random import randint

x = eval(input('How many columns?\n->'))
y = eval(input('How many lines?\n->'))


def binarygen():

    for i in range(y):

        print()
        for i in range(x):
            val = randint(0, 1)
            print(val, end=' ', flush=True)


binarygen()
