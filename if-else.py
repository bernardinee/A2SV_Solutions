#!/bin/python3

import math
import os
import random
import re
import sys



def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")


n = int(input())
check_weird(n)
