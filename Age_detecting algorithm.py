print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

meta_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15)
age = meta_age % 105
Statement = "Your age is {}; that's a good time to start programming!".format(age)
print(Statement)