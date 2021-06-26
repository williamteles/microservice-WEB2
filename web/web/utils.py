from random import randint
from datetime import datetime
import requests


def rand_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def string_to_float(text):
    dic = {".": "", ",": "."}

    for i, j in dic.items():
        text = text.replace(i, j)
    
    return float(text)
