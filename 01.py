import sys
from helpers import read_data_file

print('\n************* Day 01 *************\n')

expenses = read_data_file(sys.argv[1], convert=int)
answer = None

for i in range(len(expenses)):
    j = i + 1
    while j < len(expenses):
        k = j + 1
        while k < len(expenses):
            if ((expenses[i] + expenses[j] + expenses[k]) == 2020):
                answer = expenses[i] * expenses[j] * expenses[k]
            k = k + 1
        j = j + 1

print(answer)
