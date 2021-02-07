"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730246800"


# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...
print("Your fortune cookie says...")

random_saying: int = randint(1, 4)


if random_saying == 1:
    print('you have a bright future ')
else:
    if random_saying == 2:
        print("money is coming your way")
    if random_saying == 3:
        print('good grades are coming your way')
    if random_saying == 4:
        print ('you will have a lucky day')


print("Now, go spread positive vibes!")
