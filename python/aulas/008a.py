from math import sqrt, floor
import random
import emoji

num = random.randint(1, 10)
raiz = sqrt(num)
print('A raiz de {} é {}.'.format(num, floor(raiz)))
print(emoji.emojize('Python is :thumbsup:', language='alias'))