from random import randint


random_numberg = randint(1, 100)
print('Угадайте число от 1 до 100!')

def g():
    while True:
        if int(input()) < random_numberg:
            print('Ваше число меньше того, что загадано!')
        elif int(input()) > random_numberg:
            print('Ваше число больше того, что загадано!')
        elif int(input()) == random_numberg:
            print('Отличная интуиция! Вы угадали число!')
            break
        

    