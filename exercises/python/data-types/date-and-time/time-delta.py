#!/bin/python3

import os
from datetime import datetime


def time_delta(t1, t2):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    start_date = datetime.strptime(t1, date_format)
    end_date = datetime.strptime(t2, date_format)
    delta = start_date - end_date
    return str(int(abs(delta.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
