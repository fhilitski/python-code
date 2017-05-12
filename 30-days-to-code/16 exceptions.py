#!/bin/python3

import sys


S = input().strip()
try:
    print(int(S))
except BaseException:
    print("Bad String")
