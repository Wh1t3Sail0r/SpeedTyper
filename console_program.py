import time as t
from time import *
import numpy as np


def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix[x, y] = matrix[x-1, y-1]

            else:
                matrix[x, y] = min(matrix[x-1, y], matrix[x-1, y-1], matrix[x, y-1]) + 1

    print(matrix)
    return matrix[size_x - 1, size_y - 1]


def get_word():
    return 'abcde'


original = get_word()
print(original)


def split(word):
    return [char for char in word]


start = str(input('Press enter to start!'))

start = t.time()
answer = str(input(''))
end = t.time()
time_taken = end-start


test = split(answer)
check = split(original)
words = answer.split(' ')
print(len(words))

check_test = len(check) > len(test)
test_check = len(test) > len(check)

count = levenshtein(check, test)
print(count)

acc = round(float(1 - (count/(len(check)))) * 100, 2)

print(acc, '% accurate')
print("it took", time_taken, "seconds")
print('Words per minute: ', round((len(words)/time_taken*60)), 'wpm')

