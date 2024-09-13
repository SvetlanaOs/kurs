import random

x = random.randint(3, 20)
print('число', x)
result = ''
for i in range(1, x // 2+1):
    for j in range(i + 1, x ):
        if x % (i + j) == 0:
            result = result + str(i) + str(j)
print('пароль:',result)
