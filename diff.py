import os
import re
from random import *

test_times = 100  # number of testcases
line_num = 100  # line number of each testcase

proj3exe_filename_1 = 'proj3exe_kza'
proj3exe_filename_2 = 'proj3exe_wsy'

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
        f.write('print\n')
    f.write('quit\n')
    f.close()

    if os.system('./{} < random_test_{}.txt > {}_output_{}.txt'.format(proj3exe_filename_1,test, proj3exe_filename_1, test)) != 0:
        print('{} test #{} {}'.format(proj3exe_filename_1, test, 'error'))
        exit()

    if os.system('./{} < random_test_{}.txt > {}_output_{}.txt'.format(proj3exe_filename_2,test, proj3exe_filename_2, test)) != 0:
        print('{} test #{} {}'.format(proj3exe_filename_2, test, 'error'))
        exit()

    if open('{}_output_{}.txt'.format(proj3exe_filename_1,test)).read() == open('{}_output_{}.txt'.format(proj3exe_filename_2,test)).read():
        os.remove('{}_output_{}.txt'.format(proj3exe_filename_1,test))
        os.remove('{}_output_{}.txt'.format(proj3exe_filename_2,test))
        os.remove('random_test_{}.txt'.format(test))
