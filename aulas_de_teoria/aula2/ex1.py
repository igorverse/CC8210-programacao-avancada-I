from random import randrange

i = 0
higher = 0
times = 0
while i <= 10:
    number = randrange(1, 101)
    actual = number
    print(number)
    if (actual > higher):
        higher = actual
        times += 1
    i += 1

print('higher:', higher)
print('showed:', times, 'times')