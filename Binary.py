from random import randint

input_x = eval(input('How many columns?\n->'))
input_y = eval(input('How many lines?\n->'))


def binarygen(x, y):

    for i in range(y):

        print()
        for i in range(x):
            val = randint(0, 1)
            print(val, end=' ', flush=True)


binarygen(input_x, input_y)
