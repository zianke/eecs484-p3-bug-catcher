import os
import re
from random import *

test_times = 100  # number of testcases
line_num = 100  # line number of each testcase

for test in range(test_times):
    data = set()
    correct_results = []
    f = open('random_test_{}.txt'.format(test), 'w+')
    for i in range(line_num):
        command = randint(0, 100)
        num = randint(-100, 100)

        if command % 3 == 0:
            f.write('delete ' + str(num) + '\n')
            data.discard(num)
        elif command % 10 != 0:
            f.write('insert ' + str(num) + '\n')
            data.add(num)
        else:
            num2 = randint(num, num + 50)
            f.write('find ' + str(num) + ' ' + str(num2) + '\n')
            found = list(filter(lambda x: num <= x and x <= num2, data))
            correct_results.append(sorted(found))

    f.write('quit\n')
    f.close()

    f = open('correct_output_{}.txt'.format(test), 'w+')
    for correct_result in correct_results:
        f.write('@@@     {}\n\n'.format(str(correct_result).replace('[', '[ ').replace(']', ' ]').replace(',', ' |')))
    f.close()

    if os.system('./proj3exe < random_test_{}.txt > my_output_{}.txt 2> my_error_{}.txt'.format(test, test, test)) != 0:
        print('test #{} {}'.format(test, 'error'))
        continue

    os.remove('my_error_{}.txt'.format(test))

    f = open('my_output_{}.txt'.format(test))
    my_output = f.readlines()
    f.close()

    my_results = []
    for line in my_output:
        if line.startswith('@@@'):
            result = list(map(lambda str: int(str), re.findall(r'[\[|] (-?\d+)', line)))
            my_results.append(result)

    if my_results == correct_results:
        os.remove('my_output_{}.txt'.format(test))
        os.remove('random_test_{}.txt'.format(test))
        os.remove('correct_output_{}.txt'.format(test))

    print('test #{} {}'.format(test, 'passed' if my_results == correct_results else 'failed'))
