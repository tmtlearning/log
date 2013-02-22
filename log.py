import math

INPUT = 'input.txt'


def countLog(arr):
    a1p = []
    a10 = []
    for number in arr:
        try:
            number = int(number)
        except ValueError:
            #print('n/a')
            continue

        a1p.append(math.log1p(number))
        a10.append(math.log10(number))
        for x in range(1, len(a1p)):
            #print ('%s %s' % ('ln','lg'))
            print ('%4f %4f' % (a1p[x], a10[x]))


while input('Do you want to exit? ') != 'yes':
    zzz = input('Enter filename: ')
    print(zzz)
    try:
        with open(str(zzz), 'r') as file_in:
            data = file_in.readlines()
            file_in.close()
            countLog(data)
    except FileNotFoundError:
        print('Oops! File not found! Try again\n')
input('Bye!')
