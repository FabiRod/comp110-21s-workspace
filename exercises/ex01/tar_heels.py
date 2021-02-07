"""An exercise in remainders and boolean logic."""

__author__ = "730246800"



# Begin your solution here...
my_num = int(input('Enter an int: '))

if my_num % 2 == 0 and my_num % 7 == 0:
    print ('TAR HEELS')
elif  my_num % 2 == 0:
    print ('TAR')
elif  my_num % 7 == 0:
    print ('HEELS')
else: 
    print ('CAROLINA')

